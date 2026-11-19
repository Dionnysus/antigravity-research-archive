"""
╔══════════════════════════════════════════════════════════════════════════════╗
║          Vietnamese Technical Document Translator — main.py                 ║
║                                                                              ║
║  Architecture: Async NLP Pipeline with Smart Chunking, Glossary Injection,  ║
║  Exponential Backoff Retry, Concurrency Control, and Rich Progress UI        ║
╚══════════════════════════════════════════════════════════════════════════════╝

Dependencies:
    pip install aiohttp tiktoken rich tenacity

Usage:
    python main.py --input document.md --glossary glossary.json --output output_translated.md

Glossary file format (glossary.json):
    {
        "machine learning": "học máy",
        "neural network": "mạng nơ-ron",
        "pipeline": "pipeline",
        "deployment": "triển khai"
    }
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import os
import re
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import aiohttp
import tiktoken
from rich.console import Console
from rich.logging import RichHandler
from rich.panel import Panel
from rich.progress import (
    BarColumn,
    MofNCompleteColumn,
    Progress,
    SpinnerColumn,
    TaskID,
    TextColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
)
from rich.table import Table
from rich.text import Text
from tenacity import (
    AsyncRetrying,
    RetryError,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

# ──────────────────────────────────────────────────────────────────────────────
# Constants & Configuration
# ──────────────────────────────────────────────────────────────────────────────

DEFAULT_MODEL: str = "gpt-4o"
DEFAULT_MAX_TOKENS: int = 1500          # tokens per chunk (input)
DEFAULT_CONCURRENCY: int = 5            # max simultaneous API calls
DEFAULT_MAX_RETRIES: int = 5
DEFAULT_BACKOFF_MIN: float = 1.0        # seconds
DEFAULT_BACKOFF_MAX: float = 60.0       # seconds
TIKTOKEN_MODEL: str = "cl100k_base"
OPENAI_API_URL: str = "https://api.openai.com/v1/chat/completions"

# Supported input formats
SUPPORTED_EXTENSIONS: frozenset[str] = frozenset({".txt", ".md", ".pdf"})

SYSTEM_PROMPT_TEMPLATE: str = """Bạn là một Dịch giả Kỹ thuật cấp cao chuyên ngành Khoa học Máy tính. Nhiệm vụ của bạn là dịch văn bản sau sang tiếng Việt.
Tuân thủ NGHIÊM NGẶT các quy chuẩn sau:

1. TRUYỀN TẢI CHÍNH XÁC: Dịch đúng 100% ý đồ học thuật và kỹ thuật của tác giả. Giữ văn phong khúc chiết, mạch lạc. Tuyệt đối không dịch word-by-word gây tối nghĩa.

2. GLOSSARY BẮT BUỘC: Dưới đây là từ điển thuật ngữ {glossary_data}. Tuân thủ tuyệt đối từ điển này.

3. TỪ KHÓA CHUYÊN NGÀNH: Các từ khóa nền tảng như Agile, Framework, Use case, Module... phải giữ nguyên tiếng Anh. Với thuật ngữ tiếng Việt có tính chuyên ngành cao, giữ nguyên từ gốc tiếng Anh trong ngoặc đơn ở lần xuất hiện đầu (vd: Lập trình hướng đối tượng (Object-Oriented Programming)).

4. BẢO TOÀN CODE & ĐỊNH DẠNG: Tuyệt đối KHÔNG dịch các đoạn code, tên hàm, tên biến, thẻ tag, hoặc cấu trúc Markdown. Giữ nguyên 100% các ký tự in đậm, in nghiêng, danh sách.

Chỉ trả lời bằng bản dịch tiếng Việt, không thêm giải thích hay chú thích ngoài lề."""

# Retryable HTTP status codes
RETRYABLE_STATUS_CODES: frozenset[int] = frozenset({429, 500, 502, 503, 504})

# ──────────────────────────────────────────────────────────────────────────────
# Windows UTF-8 Fix
# Force UTF-8 on stdout/stderr so that Rich emoji render correctly on Windows
# terminals that default to cp1252 (legacy code page).
# ──────────────────────────────────────────────────────────────────────────────

if sys.platform == "win32":
    import io
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[union-attr]
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[union-attr]

# ──────────────────────────────────────────────────────────────────────────────
# Logging Setup
# ──────────────────────────────────────────────────────────────────────────────

console = Console(stderr=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(console=console, rich_tracebacks=True, show_path=False)],
)
log = logging.getLogger("translator")


# ──────────────────────────────────────────────────────────────────────────────
# Data Models
# ──────────────────────────────────────────────────────────────────────────────

@dataclass
class TranslationConfig:
    """Holds all runtime configuration for the translation pipeline.

    Attributes:
        input_path: Path to the source document (.txt or .md).
        output_path: Path to write the translated output (.md).
        glossary_path: Optional path to the glossary JSON file.
        api_key: OpenAI-compatible API key.
        model: Model identifier string.
        max_tokens: Maximum token budget per chunk.
        concurrency: Maximum simultaneous API requests.
        max_retries: Maximum retry attempts per chunk.
        api_base_url: Base URL for the OpenAI-compatible API.
    """

    input_path: Path
    output_path: Path
    glossary_path: Optional[Path]
    api_key: str
    model: str = DEFAULT_MODEL
    max_tokens: int = DEFAULT_MAX_TOKENS
    concurrency: int = DEFAULT_CONCURRENCY
    max_retries: int = DEFAULT_MAX_RETRIES
    api_base_url: str = OPENAI_API_URL


@dataclass
class TextChunk:
    """Represents a single text segment destined for translation.

    Attributes:
        index: Zero-based original position to guarantee reassembly order.
        text: The raw English text content.
        token_count: Approximate token count via tiktoken.
        translated_text: Populated after successful translation.
        error: Error message if all retries exhausted.
    """

    index: int
    text: str
    token_count: int
    translated_text: str = ""
    error: str = ""
    cache_hit_tokens: int = 0
    cache_miss_tokens: int = 0


@dataclass
class TranslationResult:
    """Aggregated result of the full pipeline run.

    Attributes:
        chunks: All processed chunks in original order.
        total_chunks: Total number of chunks.
        succeeded: Number of successfully translated chunks.
        failed: Number of chunks that could not be translated.
        elapsed_seconds: Total wall-clock time in seconds.
        cache_hit_tokens: Total prompt tokens served from DeepSeek prefix cache.
        cache_miss_tokens: Total prompt tokens NOT served from cache (billed normally).
    """

    chunks: list[TextChunk] = field(default_factory=list)
    total_chunks: int = 0
    succeeded: int = 0
    failed: int = 0
    elapsed_seconds: float = 0.0
    cache_hit_tokens: int = 0
    cache_miss_tokens: int = 0


# ──────────────────────────────────────────────────────────────────────────────
# Custom Exceptions
# ──────────────────────────────────────────────────────────────────────────────

class RateLimitError(Exception):
    """Raised when the API returns HTTP 429 Too Many Requests."""


class ServerError(Exception):
    """Raised when the API returns a 5xx server-side error."""


class TranslationAPIError(Exception):
    """Raised for unrecoverable API errors."""


# ──────────────────────────────────────────────────────────────────────────────
# File I/O
# ──────────────────────────────────────────────────────────────────────────────

def _read_pdf(path: Path) -> str:
    """Extract text from a PDF and convert it to structured Markdown.

    Uses PyMuPDF (fitz) for accurate text extraction. The algorithm:

    1. Iterates each page and extracts text blocks with font metadata.
    2. Detects headings by comparing each span's font size to the body
       font size (median of all spans). Spans >= 1.4x body size become
       ``#`` headings; >= 1.15x become ``##`` headings.
    3. Fixes soft-hyphen line-breaks common in PDFs (e.g. ``hyphen-\n ated``).
    4. Inserts a Markdown ``---`` page-break between pages so the chunker
       can treat page boundaries as natural split points.

    Args:
        path: Absolute path to the PDF file.

    Returns:
        A Markdown-structured string containing all extracted text.

    Raises:
        ImportError: If PyMuPDF (``pip install pymupdf``) is not installed.
        RuntimeError: If the PDF cannot be opened or is encrypted.
    """
    try:
        try:
            import pymupdf as fitz  # PyMuPDF >= 1.24 (new canonical import)
        except ImportError:
            import fitz  # PyMuPDF < 1.24 (legacy import name)
    except ImportError as exc:
        raise ImportError(
            "PyMuPDF is required to read PDF files.\n"
            "Install it with:  pip install pymupdf"
        ) from exc

    try:
        doc = fitz.open(str(path))
    except Exception as exc:
        raise RuntimeError(f"Cannot open PDF '{path}': {exc}") from exc

    if doc.is_encrypted:
        raise RuntimeError(
            f"PDF '{path}' is encrypted/password-protected. "
            "Please decrypt it before translating."
        )

    log.info(
        f"   → PDF: {doc.page_count} page(s) detected."
    )

    # ── Pass 1: collect all font sizes to determine body size (median) ──
    all_font_sizes: list[float] = []
    for page in doc:
        for block in page.get_text("dict")["blocks"]:
            if block.get("type") != 0:  # type 0 = text
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    size = span.get("size", 0)
                    if size > 4:  # ignore tiny artifact text
                        all_font_sizes.append(size)

    if not all_font_sizes:
        # Fallback: plain text extraction if no span data
        pages_text = [page.get_text("text") for page in doc]
        doc.close()
        return "\n\n---\n\n".join(pages_text)

    all_font_sizes.sort()
    body_size: float = all_font_sizes[len(all_font_sizes) // 2]  # median

    # ── Pass 2: extract text with heading detection ─────────────────────
    pages_md: list[str] = []

    for page_num, page in enumerate(doc, start=1):
        lines_out: list[str] = []
        prev_was_heading = False

        for block in page.get_text("dict")["blocks"]:
            if block.get("type") != 0:
                continue  # skip images / drawings

            block_lines: list[str] = []
            for line in block["lines"]:
                line_text_parts: list[str] = []
                max_size_in_line: float = 0.0
                is_bold_line = False

                for span in line["spans"]:
                    text = span.get("text", "").strip()
                    if not text:
                        continue
                    size = span.get("size", body_size)
                    flags = span.get("flags", 0)
                    is_bold = bool(flags & 0b10000)  # bit 4 = bold
                    line_text_parts.append(text)
                    max_size_in_line = max(max_size_in_line, size)
                    if is_bold:
                        is_bold_line = True

                if not line_text_parts:
                    continue

                joined = " ".join(line_text_parts)

                # Fix soft-hyphen line-breaks: "hyphen-\nated" -> "hyphenated"
                joined = re.sub(r"-\s+", lambda m: "" if len(m.group(0)) > 1 else m.group(0), joined)

                # Determine Markdown heading level by relative font size
                ratio = max_size_in_line / body_size if body_size else 1.0
                if ratio >= 1.4 and (is_bold_line or ratio >= 1.6):
                    joined = f"# {joined}"
                    prev_was_heading = True
                elif ratio >= 1.15 and is_bold_line:
                    joined = f"## {joined}"
                    prev_was_heading = True
                else:
                    prev_was_heading = False

                block_lines.append(joined)

            if block_lines:
                lines_out.append("\n".join(block_lines))

        page_md = "\n\n".join(lines_out)
        # Prepend page marker (useful for debugging large docs)
        pages_md.append(f"<!-- Page {page_num} -->\n{page_md}")

    doc.close()
    return "\n\n---\n\n".join(pages_md)


def read_source_document(path: Path) -> str:
    """Read a .txt, .md, or .pdf file and return its content as plain text / Markdown.

    Dispatches to format-specific parsers:
    - ``.txt`` / ``.md`` — UTF-8 text read directly.
    - ``.pdf``           — PyMuPDF extraction with heading detection.

    Args:
        path: Absolute or relative path to the source file.

    Returns:
        The full text content as a string, ready for chunking.

    Raises:
        ValueError: If the file extension is not in SUPPORTED_EXTENSIONS.
        FileNotFoundError: If the file does not exist.
        ImportError: If pymupdf is not installed (PDF only).
        RuntimeError: If the PDF is encrypted or unreadable (PDF only).
    """
    ext = path.suffix.lower()
    if ext not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file format '{path.suffix}'. "
            f"Supported: {', '.join(sorted(SUPPORTED_EXTENSIONS))}"
        )
    if not path.exists():
        raise FileNotFoundError(f"Source document not found: {path}")

    log.info(f"📄 Reading source document: [bold]{path}[/bold]", extra={"markup": True})

    if ext == ".pdf":
        content = _read_pdf(path)
    else:
        content = path.read_text(encoding="utf-8")

    log.info(f"   → {len(content):,} characters extracted.")
    return content


def load_glossary(path: Optional[Path]) -> dict[str, str]:
    """Load and validate a glossary JSON file.

    Args:
        path: Path to the glossary JSON file, or None to skip.

    Returns:
        A dictionary mapping English terms to Vietnamese translations.
        Returns an empty dict if path is None.

    Raises:
        FileNotFoundError: If the specified glossary file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
        TypeError: If the JSON root is not a flat string to string dictionary.
    """
    if path is None:
        log.info("ℹ️  No glossary file provided. Proceeding without glossary.")
        return {}

    if not path.exists():
        raise FileNotFoundError(f"Glossary file not found: {path}")

    log.info(f"📖 Loading glossary: [bold]{path}[/bold]", extra={"markup": True})
    raw = path.read_text(encoding="utf-8")
    data: object = json.loads(raw)

    if not isinstance(data, dict):
        raise TypeError("Glossary JSON root must be a dict (object), not a list or scalar.")

    for key, value in data.items():
        if not isinstance(key, str) or not isinstance(value, str):
            raise TypeError(
                f"Glossary entries must be string to string pairs. "
                f"Found: {type(key).__name__!r} -> {type(value).__name__!r}"
            )

    log.info(f"   → {len(data):,} glossary entries loaded.")
    return data  # type: ignore[return-value]


def write_output_document(path: Path, content: str) -> None:
    """Write the translated Markdown content to the output file.

    Args:
        path: Destination file path (will be created or overwritten).
        content: The complete translated Markdown string.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    log.info(f"✅ Output written to: [bold green]{path}[/bold green]", extra={"markup": True})


# ──────────────────────────────────────────────────────────────────────────────
# Smart Chunking
# ──────────────────────────────────────────────────────────────────────────────

def _split_into_logical_blocks(text: str) -> list[str]:
    """Split raw text into logical blocks at Markdown headings or blank lines.

    This pre-pass preserves paragraph and heading structure before token-aware
    chunking, preventing headings from being stranded at the tail of a chunk.

    Args:
        text: The full source document text.

    Returns:
        A list of non-empty logical block strings.
    """
    # Split on blank lines OR immediately before a Markdown heading (#, ##, ...)
    heading_re = re.compile(r"(?m)(?=^#{1,6}\s)", flags=re.MULTILINE)
    segments: list[str] = []
    for heading_block in heading_re.split(text):
        for paragraph in re.split(r"\n{2,}", heading_block):
            stripped = paragraph.strip()
            if stripped:
                segments.append(stripped)
    return segments


def _split_into_sentences(text: str) -> list[str]:
    """Heuristically split a paragraph into sentences.

    Handles common English sentence-ending punctuation while avoiding false
    splits on abbreviations like 'e.g.', 'i.e.', 'vs.', 'Dr.', etc.

    Args:
        text: A block of text (typically a single paragraph).

    Returns:
        A list of sentences, each stripped of leading/trailing whitespace.
    """
    # Abbreviation safeguard: temporarily replace known abbreviation periods
    abbrev_re = re.compile(
        r"\b(e\.g|i\.e|vs|Dr|Mr|Mrs|Ms|Prof|Sr|Jr|etc|Fig|vol|no|pp|ca)\.",
        re.IGNORECASE,
    )
    placeholder_text = abbrev_re.sub(r"\1<PERIOD>", text)

    # Split on sentence-ending punctuation followed by whitespace + capital letter
    sentence_re = re.compile(r"(?<=[.!?])\s+(?=[A-Z\"\'`])")
    raw_sentences = sentence_re.split(placeholder_text)

    # Restore abbreviation periods
    return [s.replace("<PERIOD>", ".").strip() for s in raw_sentences if s.strip()]


def chunk_text(text: str, max_tokens: int = DEFAULT_MAX_TOKENS) -> list[TextChunk]:
    """Partition source text into token-bounded chunks without cutting sentences.

    Algorithm:
        1. Split the document into logical blocks (heading-aware).
        2. For each block, tokenise and greedily accumulate sentences into a
           running buffer until the next sentence would exceed ``max_tokens``.
        3. When a single sentence exceeds ``max_tokens``, emit it as its own
           chunk (necessary to avoid infinite loops).
        4. Assign stable 0-based indices to every emitted chunk.

    Args:
        text: Full source document text.
        max_tokens: Maximum tiktoken token count per chunk.

    Returns:
        An ordered list of :class:`TextChunk` instances ready for translation.
    """
    enc = tiktoken.get_encoding(TIKTOKEN_MODEL)

    def count_tokens(s: str) -> int:
        return len(enc.encode(s))

    blocks = _split_into_logical_blocks(text)
    chunks: list[TextChunk] = []
    buffer: list[str] = []
    buffer_tokens: int = 0
    chunk_index: int = 0

    def flush_buffer() -> None:
        nonlocal buffer, buffer_tokens, chunk_index
        if buffer:
            joined = "\n\n".join(buffer)
            chunks.append(
                TextChunk(
                    index=chunk_index,
                    text=joined,
                    token_count=buffer_tokens,
                )
            )
            chunk_index += 1
            buffer = []
            buffer_tokens = 0

    for block in blocks:
        sentences = _split_into_sentences(block)
        for sentence in sentences:
            sentence_tokens = count_tokens(sentence)

            # Edge case: single sentence exceeds budget -> emit standalone
            if sentence_tokens > max_tokens:
                flush_buffer()
                chunks.append(
                    TextChunk(
                        index=chunk_index,
                        text=sentence,
                        token_count=sentence_tokens,
                    )
                )
                chunk_index += 1
                continue

            # Would adding this sentence overflow the buffer?
            if buffer_tokens + sentence_tokens > max_tokens:
                flush_buffer()

            buffer.append(sentence)
            buffer_tokens += sentence_tokens

    flush_buffer()

    log.info(
        f"✂️  Chunking complete: [bold]{len(chunks)}[/bold] chunks "
        f"(max {max_tokens} tokens each)",
        extra={"markup": True},
    )
    return chunks


# ──────────────────────────────────────────────────────────────────────────────
# Prompt Builder
# ──────────────────────────────────────────────────────────────────────────────

def build_system_prompt(glossary: dict[str, str]) -> str:
    """Serialise the glossary and inject it into the system prompt template.

    Args:
        glossary: Mapping of English terms to Vietnamese equivalents.

    Returns:
        The fully rendered system prompt string ready for the API payload.
    """
    if glossary:
        # Sort keys for a deterministic byte sequence → stable prefix hash across runs.
        # If keys are unsorted, reordering in glossary.json invalidates the DeepSeek
        # prefix cache even when the content is semantically identical.
        sorted_glossary = dict(sorted(glossary.items()))
        glossary_str = json.dumps(sorted_glossary, ensure_ascii=False, indent=2)
        glossary_data = f"\n```json\n{glossary_str}\n```"
    else:
        glossary_data = " (Không có từ điển được cung cấp cho phiên này.)"

    return SYSTEM_PROMPT_TEMPLATE.format(glossary_data=glossary_data)


def build_api_payload(
    chunk_text_content: str,
    system_prompt: str,
    model: str,
    max_output_tokens: int = 4096,
) -> dict:
    """Construct the OpenAI Chat Completions API request payload.

    Args:
        chunk_text_content: The English text segment to translate.
        system_prompt: Pre-rendered system prompt with injected glossary.
        model: OpenAI model identifier (e.g. 'gpt-4o').
        max_output_tokens: Maximum tokens in the model response.

    Returns:
        A dictionary suitable for JSON serialisation and POSTing to the API.
    """
    # NOTE: DeepSeek Automatic Prefix Caching (APC) caches the KV-state of the
    # longest common prompt prefix across requests.  To maximise cache hits:
    #   1. system message (large, static) → placed FIRST in messages list.
    #   2. user message (small, dynamic)  → placed LAST.
    #   3. Only `temperature` is set — DeepSeek recommends NOT combining
    #      temperature + top_p as it can alter sampling and may affect cache
    #      key consistency.  top_p is omitted intentionally.
    return {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": chunk_text_content},
        ],
        "max_tokens": max_output_tokens,
        "temperature": 0.2,
    }


# ──────────────────────────────────────────────────────────────────────────────
# Async Translation Engine
# ──────────────────────────────────────────────────────────────────────────────

async def translate_chunk(
    session: aiohttp.ClientSession,
    semaphore: asyncio.Semaphore,
    chunk: TextChunk,
    system_prompt: str,
    config: TranslationConfig,
    progress: Progress,
    task_id: TaskID,
) -> TextChunk:
    """Translate a single :class:`TextChunk` with retries and backoff.

    Implements an exponential backoff retry strategy via ``tenacity`` for
    HTTP 429 (rate limit) and 5xx (server error) responses. Uses the shared
    ``asyncio.Semaphore`` to cap concurrent in-flight requests.

    Args:
        session: Shared ``aiohttp.ClientSession`` for connection pooling.
        semaphore: Concurrency gate acquired before each API call.
        chunk: The text chunk to translate; mutated in place on success/failure.
        system_prompt: Pre-rendered system prompt with glossary.
        config: Pipeline configuration (API key, model, URL, retry params).
        progress: Rich Progress instance for real-time status updates.
        task_id: The Rich task ID associated with the overall translation bar.

    Returns:
        The same ``chunk`` object, with ``translated_text`` or ``error`` set.
    """
    payload = build_api_payload(chunk.text, system_prompt, config.model)
    headers = {
        "Authorization": f"Bearer {config.api_key}",
        "Content-Type": "application/json",
    }

    async with semaphore:
        try:
            async for attempt in AsyncRetrying(
                retry=retry_if_exception_type((RateLimitError, ServerError)),
                stop=stop_after_attempt(config.max_retries),
                wait=wait_exponential(
                    multiplier=1,
                    min=DEFAULT_BACKOFF_MIN,
                    max=DEFAULT_BACKOFF_MAX,
                ),
                reraise=False,
            ):
                with attempt:
                    attempt_number = attempt.retry_state.attempt_number
                    if attempt_number > 1:
                        progress.update(
                            task_id,
                            description=(
                                f"[yellow]⟳  Retry {attempt_number}/{config.max_retries} "
                                f"chunk #{chunk.index + 1}[/yellow]"
                            ),
                        )

                    async with session.post(
                        config.api_base_url,
                        json=payload,
                        headers=headers,
                    ) as response:
                        if response.status == 429:
                            retry_after = float(
                                response.headers.get("Retry-After", DEFAULT_BACKOFF_MIN)
                            )
                            log.warning(
                                f"⚠️  Rate limit hit on chunk #{chunk.index + 1}. "
                                f"Retry-After: {retry_after}s"
                            )
                            await asyncio.sleep(retry_after)
                            raise RateLimitError(
                                f"HTTP 429 on chunk #{chunk.index + 1}"
                            )

                        if response.status in RETRYABLE_STATUS_CODES:
                            raise ServerError(
                                f"HTTP {response.status} on chunk #{chunk.index + 1}"
                            )

                        if response.status != 200:
                            body = await response.text()
                            raise TranslationAPIError(
                                f"Unexpected HTTP {response.status}: {body[:200]}"
                            )

                        data = await response.json()
                        translated = data["choices"][0]["message"]["content"].strip()
                        chunk.translated_text = translated

                        # ── DeepSeek Prefix Cache telemetry ──────────────────
                        # DeepSeek returns prompt_cache_hit_tokens /
                        # prompt_cache_miss_tokens inside usage.  Other
                        # providers (OpenAI, Azure) may return
                        # prompt_tokens_details.cached_tokens instead.
                        usage = data.get("usage", {})
                        hit = (
                            usage.get("prompt_cache_hit_tokens")
                            or usage.get("prompt_tokens_details", {}).get("cached_tokens")
                            or 0
                        )
                        miss = (
                            usage.get("prompt_cache_miss_tokens")
                            # Fallback: total prompt tokens minus cached tokens
                            or (usage.get("prompt_tokens", 0) - hit)
                        )
                        chunk.cache_hit_tokens = int(hit)
                        chunk.cache_miss_tokens = int(miss)
                        if hit:
                            log.debug(
                                f"💾 Chunk #{chunk.index + 1}: "
                                f"cache hit={hit}t  miss={miss}t"
                            )

        except RetryError as exc:
            chunk.error = f"All {config.max_retries} retries exhausted: {exc}"
            log.error(
                f"❌ Chunk #{chunk.index + 1} failed after "
                f"{config.max_retries} attempts.",
                extra={"markup": True},
            )
        except TranslationAPIError as exc:
            chunk.error = str(exc)
            log.error(f"❌ Chunk #{chunk.index + 1} unrecoverable error: {exc}")
        except Exception as exc:  # noqa: BLE001
            chunk.error = f"Unexpected error: {exc}"
            log.error(f"❌ Chunk #{chunk.index + 1} unexpected error: {exc}")
        finally:
            progress.advance(task_id)

    return chunk


async def translate_all_chunks(
    chunks: list[TextChunk],
    glossary: dict[str, str],
    config: TranslationConfig,
) -> list[TextChunk]:
    """Translate all chunks concurrently under a Semaphore gate.

    Spawns one ``asyncio.Task`` per chunk. The Semaphore ensures at most
    ``config.concurrency`` tasks run simultaneously, preventing API rate limit
    overload. Results are collected in original index order for safe reassembly.

    Args:
        chunks: All source chunks from the chunking step.
        glossary: English-to-Vietnamese term dictionary.
        config: Full pipeline configuration.

    Returns:
        The same list of chunks, each with ``translated_text`` or ``error``
        populated. The list is sorted by original ``index`` for safe reassembly.
    """
    system_prompt = build_system_prompt(glossary)
    semaphore = asyncio.Semaphore(config.concurrency)

    connector = aiohttp.TCPConnector(limit=config.concurrency + 5)
    timeout = aiohttp.ClientTimeout(total=120, connect=10)

    with Progress(
        SpinnerColumn(spinner_name="dots2"),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=40, style="cyan", complete_style="green"),
        MofNCompleteColumn(),
        TimeElapsedColumn(),
        TimeRemainingColumn(),
        console=Console(),
        refresh_per_second=8,
    ) as progress:
        task_id = progress.add_task(
            description="[cyan]🔄 Translating chunks...[/cyan]",
            total=len(chunks),
        )

        async with aiohttp.ClientSession(
            connector=connector, timeout=timeout
        ) as session:
            tasks = [
                translate_chunk(
                    session=session,
                    semaphore=semaphore,
                    chunk=chunk,
                    system_prompt=system_prompt,
                    config=config,
                    progress=progress,
                    task_id=task_id,
                )
                for chunk in chunks
            ]
            results: list[TextChunk] = await asyncio.gather(*tasks)

    # Guarantee original ordering regardless of async completion order
    results.sort(key=lambda c: c.index)

    # Aggregate cache telemetry across all chunks
    total_hit = sum(c.cache_hit_tokens for c in results)
    total_miss = sum(c.cache_miss_tokens for c in results)
    if total_hit or total_miss:
        hit_rate = total_hit / (total_hit + total_miss) * 100 if (total_hit + total_miss) else 0
        log.info(
            f"[cyan]Prefix cache:[/cyan] "
            f"[green]hit={total_hit:,}t[/green]  "
            f"miss={total_miss:,}t  "
            f"rate=[bold]{hit_rate:.1f}%[/bold]",
            extra={"markup": True},
        )

    return results


# ──────────────────────────────────────────────────────────────────────────────
# Reassembly & Export
# ──────────────────────────────────────────────────────────────────────────────

def reassemble_document(chunks: list[TextChunk]) -> tuple[str, list[int]]:
    """Join translated chunks in their original order into a final document.

    Chunks that failed translation are replaced with a clearly marked error
    block containing the original English text, so the output document is
    always complete and reviewable.

    Args:
        chunks: Sorted list of processed :class:`TextChunk` instances.

    Returns:
        A tuple of:
          - The full translated Markdown string.
          - A list of indices of chunks that failed (for reporting).
    """
    parts: list[str] = []
    failed_indices: list[int] = []

    for chunk in chunks:
        if chunk.error:
            failed_indices.append(chunk.index)
            # Preserve original text inside a warning block
            fallback = (
                f"\n\n> ⚠️ **[DỊCH THUẬT THẤT BẠI — Chunk #{chunk.index + 1}]**\n"
                f"> Lỗi: {chunk.error}\n>\n"
                f"> **Nội dung gốc (tiếng Anh):**\n>\n"
                + "\n".join(f"> {line}" for line in chunk.text.splitlines())
                + "\n\n"
            )
            parts.append(fallback)
        else:
            parts.append(chunk.translated_text)

    document = "\n\n".join(parts)
    return document, failed_indices


# ──────────────────────────────────────────────────────────────────────────────
# Summary Report
# ──────────────────────────────────────────────────────────────────────────────

def print_summary(result: TranslationResult, output_path: Path) -> None:
    """Render a formatted summary table to the terminal via Rich.

    Args:
        result: Aggregated translation result metadata.
        output_path: Path where the translated document was written.
    """
    status_color = "green" if result.failed == 0 else "yellow"
    status_icon = "✅" if result.failed == 0 else "⚠️"

    table = Table(
        title=f"{status_icon} Translation Complete",
        title_style=f"bold {status_color}",
        show_header=True,
        header_style="bold dim",
        border_style="dim",
        expand=False,
        min_width=50,
    )
    table.add_column("Metric", style="dim", min_width=22)
    table.add_column("Value", style="bold", justify="right")

    table.add_row("Total chunks", str(result.total_chunks))
    table.add_row("✔ Succeeded", f"[green]{result.succeeded}[/green]")
    table.add_row(
        "✘ Failed",
        f"[red]{result.failed}[/red]" if result.failed > 0 else "[green]0[/green]",
    )
    table.add_row("⏱ Elapsed", f"{result.elapsed_seconds:.1f}s")

    # DeepSeek prefix-cache telemetry (only shown when data is available)
    total_cache_tokens = result.cache_hit_tokens + result.cache_miss_tokens
    if total_cache_tokens > 0:
        hit_rate = result.cache_hit_tokens / total_cache_tokens * 100
        cache_color = "green" if hit_rate >= 80 else "yellow" if hit_rate >= 40 else "red"
        table.add_row(
            "💾 Cache hit tokens",
            f"[{cache_color}]{result.cache_hit_tokens:,}t ({hit_rate:.1f}%)[/{cache_color}]",
        )
        table.add_row(
            "   Cache miss tokens",
            f"{result.cache_miss_tokens:,}t",
        )

    table.add_row("📁 Output file", str(output_path))

    Console().print(table)


# ──────────────────────────────────────────────────────────────────────────────
# CLI Argument Parser
# ──────────────────────────────────────────────────────────────────────────────

def parse_args() -> TranslationConfig:
    """Parse command-line arguments and build a :class:`TranslationConfig`.

    Reads the ``OPENAI_API_KEY`` environment variable for the API key.

    Returns:
        A fully populated :class:`TranslationConfig` instance.

    Raises:
        SystemExit: If required arguments are missing or validation fails.
    """
    parser = argparse.ArgumentParser(
        prog="main.py",
        description=(
            "🌐 Vietnamese Technical Document Translator\n"
            "   Async NLP pipeline — English (.txt/.md) -> Vietnamese (.md)"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python main.py --input README.md --glossary glossary.json\n"
            "  python main.py --input doc.txt --output result.md --concurrency 3\n"
            "\n"
            "Environment variables:\n"
            "  OPENAI_API_KEY   Your OpenAI (or compatible) API key (required)\n"
            "  OPENAI_BASE_URL  Override the API endpoint URL (optional)\n"
        ),
    )

    parser.add_argument(
        "--input", "-i",
        required=True,
        type=Path,
        metavar="FILE",
        help="Path to the source .txt or .md document",
    )
    parser.add_argument(
        "--output", "-o",
        type=Path,
        metavar="FILE",
        default=None,
        help="Output .md file path (default: <input_stem>_translated.md)",
    )
    parser.add_argument(
        "--glossary", "-g",
        type=Path,
        metavar="FILE",
        default=None,
        help="Path to glossary.json (optional)",
    )
    parser.add_argument(
        "--model", "-m",
        default=DEFAULT_MODEL,
        help=f"OpenAI model ID (default: {DEFAULT_MODEL})",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=DEFAULT_MAX_TOKENS,
        metavar="N",
        help=f"Max tokens per chunk (default: {DEFAULT_MAX_TOKENS})",
    )
    parser.add_argument(
        "--concurrency", "-c",
        type=int,
        default=DEFAULT_CONCURRENCY,
        metavar="N",
        help=f"Max concurrent API calls (default: {DEFAULT_CONCURRENCY})",
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=DEFAULT_MAX_RETRIES,
        metavar="N",
        help=f"Max retry attempts per chunk (default: {DEFAULT_MAX_RETRIES})",
    )

    args = parser.parse_args()

    api_key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not api_key:
        parser.error(
            "API key not found. Set the OPENAI_API_KEY environment variable.\n"
            "  PowerShell:  $env:OPENAI_API_KEY = 'sk-...'\n"
            "  Bash/Zsh:    export OPENAI_API_KEY='sk-...'"
        )

    api_base_url = os.environ.get("OPENAI_BASE_URL", OPENAI_API_URL).strip()

    output_path: Path = args.output or (
        args.input.parent / f"{args.input.stem}_translated.md"
    )

    return TranslationConfig(
        input_path=args.input.resolve(),
        output_path=output_path.resolve(),
        glossary_path=args.glossary.resolve() if args.glossary else None,
        api_key=api_key,
        model=args.model,
        max_tokens=args.max_tokens,
        concurrency=args.concurrency,
        max_retries=args.max_retries,
        api_base_url=api_base_url,
    )


# ──────────────────────────────────────────────────────────────────────────────
# Main Async Entry Point
# ──────────────────────────────────────────────────────────────────────────────

async def main() -> None:
    """Orchestrate the full end-to-end translation pipeline.

    Pipeline stages:
        1. Parse CLI arguments -> :class:`TranslationConfig`
        2. Read source document -> raw text
        3. Load optional glossary -> term dictionary
        4. Smart-chunk the text -> list of :class:`TextChunk`
        5. Async-translate all chunks with retry/backoff
        6. Reassemble chunks in original order
        7. Write output Markdown file
        8. Print summary report

    Raises:
        SystemExit: On unrecoverable I/O or configuration errors.
    """
    Console().print(
        Panel.fit(
            Text.from_markup(
                "[bold cyan]🌐 Vietnamese Technical Document Translator[/bold cyan]\n"
                "[dim]Async NLP Pipeline  •  Smart Chunking  •  Glossary Injection[/dim]"
            ),
            border_style="cyan",
            padding=(0, 2),
        )
    )

    # ── Stage 1: Configuration ──────────────────────────────────────────────
    try:
        config = parse_args()
    except SystemExit:
        raise

    # ── Stage 2: File I/O ───────────────────────────────────────────────────
    try:
        source_text = read_source_document(config.input_path)
        glossary = load_glossary(config.glossary_path)
    except (FileNotFoundError, ValueError, TypeError, json.JSONDecodeError) as exc:
        log.critical(
            f"[red]Fatal I/O error:[/red] {exc}", extra={"markup": True}
        )
        sys.exit(1)

    if not source_text.strip():
        log.critical("Source document is empty. Nothing to translate.")
        sys.exit(1)

    # ── Stage 3: Chunking ───────────────────────────────────────────────────
    chunks = chunk_text(source_text, config.max_tokens)

    if not chunks:
        log.critical("Chunking produced zero chunks. Check your input file.")
        sys.exit(1)

    # ── Stage 4: Async Translation ──────────────────────────────────────────
    start_time = time.monotonic()
    log.info(
        f"🚀 Starting async translation: [bold]{len(chunks)}[/bold] chunks  "
        f"│  concurrency=[bold]{config.concurrency}[/bold]  "
        f"│  model=[bold]{config.model}[/bold]",
        extra={"markup": True},
    )

    translated_chunks = await translate_all_chunks(chunks, glossary, config)
    elapsed = time.monotonic() - start_time

    # ── Stage 5: Reassembly ─────────────────────────────────────────────────
    final_document, failed_indices = reassemble_document(translated_chunks)

    # ── Stage 6: Export ─────────────────────────────────────────────────────
    try:
        write_output_document(config.output_path, final_document)
    except OSError as exc:
        log.critical(f"Failed to write output file: {exc}")
        sys.exit(1)

    # ── Stage 7: Summary ────────────────────────────────────────────────────
    result = TranslationResult(
        chunks=translated_chunks,
        total_chunks=len(translated_chunks),
        succeeded=len(translated_chunks) - len(failed_indices),
        failed=len(failed_indices),
        elapsed_seconds=elapsed,
        cache_hit_tokens=sum(c.cache_hit_tokens for c in translated_chunks),
        cache_miss_tokens=sum(c.cache_miss_tokens for c in translated_chunks),
    )
    print_summary(result, config.output_path)

    if failed_indices:
        Console().print(
            f"[yellow]⚠️  {len(failed_indices)} chunk(s) failed to translate "
            f"(indices: {[i + 1 for i in failed_indices]}). "
            f"Check the output file for inline error blocks.[/yellow]"
        )
        sys.exit(2)  # Non-zero exit to signal partial failure


if __name__ == "__main__":
    asyncio.run(main())
