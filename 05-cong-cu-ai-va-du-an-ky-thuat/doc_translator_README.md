# 🌐 Vietnamese Technical Document Translator

An **async NLP pipeline** for translating English IT/CS technical documents into Vietnamese using the OpenAI API (or any compatible endpoint).

---

## ✨ Features

| Feature | Detail |
|---|---|
| **Smart Chunking** | Token-aware splitting (tiktoken `cl100k_base`) — never cuts sentences, respects Markdown headings |
| **Async Engine** | `asyncio` + `aiohttp` for concurrent API calls |
| **Rate Limit Safety** | `asyncio.Semaphore` caps concurrency; exponential backoff retry via `tenacity` |
| **Glossary Injection** | Reads `glossary.json` → injects into System Prompt every call |
| **Ordered Reassembly** | Chunks always stitched back in original order |
| **Rich Progress UI** | Live progress bar, spinner, ETA, per-chunk retry status |
| **Error Recovery** | Failed chunks marked inline in output (original English preserved) |

---

## 📦 Installation

```bash
pip install aiohttp tiktoken rich tenacity
```

> **Python ≥ 3.10** required.

---

## 🔑 API Key Setup

```powershell
# PowerShell
$env:OPENAI_API_KEY = "sk-..."

# Use a different endpoint (e.g. Azure OpenAI, local Ollama)
$env:OPENAI_BASE_URL = "https://your-endpoint/v1/chat/completions"
```

---

## 🚀 Usage

```bash
# Basic usage
python main.py --input document.md --glossary glossary.json

# Full options
python main.py \
  --input    README.md          \   # Source .txt or .md file
  --output   result_vi.md       \   # Output file (default: <name>_translated.md)
  --glossary glossary.json      \   # Optional term dictionary
  --model    gpt-4o             \   # OpenAI model (default: gpt-4o)
  --max-tokens 1500             \   # Max tokens per chunk (default: 1500)
  --concurrency 5               \   # Parallel API calls (default: 5)
  --max-retries 5                   # Retry attempts per chunk (default: 5)
```

---

## 📖 Glossary File Format

Create a `glossary.json` with English → Vietnamese term pairs:

```json
{
  "machine learning": "học máy",
  "neural network": "mạng nơ-ron",
  "pipeline": "pipeline",
  "deployment": "triển khai",
  "latency": "độ trễ",
  "throughput": "thông lượng"
}
```

The entire glossary is serialized and injected into the **System Prompt** on every API call, forcing the model to use your preferred translations consistently.

---

## 🏗️ Pipeline Architecture

```
┌─────────────┐    ┌──────────────────┐    ┌────────────────────────────┐
│ Source File │───▶│  Smart Chunking  │───▶│   Async Translation Pool   │
│ (.txt/.md)  │    │  (tiktoken-aware)│    │  ┌──────┐  ┌──────┐        │
└─────────────┘    │  • No sentence   │    │  │Chunk │  │Chunk │  ...   │
                   │    cuts          │    │  │  #1  │  │  #2  │        │
┌─────────────┐    │  • Heading-aware │    │  └──┬───┘  └──┬───┘        │
│ Glossary    │───▶│                  │    │     │  Semaphore│           │
│ (.json)     │    └──────────────────┘    │     │  (max N)  │           │
└─────────────┘                           │  ┌──▼───────────▼──┐        │
       │                                  │  │  aiohttp POST   │        │
       │  injected into System Prompt     │  │  + tenacity     │        │
       └─────────────────────────────────▶│  │  retry/backoff  │        │
                                          │  └─────────────────┘        │
                                          └────────────────┬───────────┘
                                                           │
                                          ┌────────────────▼───────────┐
                                          │  Ordered Reassembly        │
                                          │  (sort by chunk.index)     │
                                          └────────────────┬───────────┘
                                                           │
                                          ┌────────────────▼───────────┐
                                          │  output_translated.md      │
                                          └────────────────────────────┘
```

---

## 🧩 Code Structure

```
main.py
├── Constants & Config (TranslationConfig dataclass)
├── Data Models        (TextChunk, TranslationResult)
├── Custom Exceptions  (RateLimitError, ServerError, TranslationAPIError)
├── File I/O
│   ├── read_source_document()   — UTF-8 safe file reader
│   ├── load_glossary()          — JSON validation + loading
│   └── write_output_document()  — UTF-8 file writer
├── Smart Chunking
│   ├── _split_into_logical_blocks()  — Heading-aware pre-split
│   ├── _split_into_sentences()       — Abbreviation-safe sentence split
│   └── chunk_text()                  — Token-budget greedy chunking
├── Prompt Builder
│   ├── build_system_prompt()    — Glossary serialization + injection
│   └── build_api_payload()      — OpenAI payload construction
├── Async Translation Engine
│   ├── translate_chunk()        — Single chunk + tenacity retry
│   └── translate_all_chunks()   — asyncio.gather + Semaphore gate
├── Reassembly
│   └── reassemble_document()    — Sorted join + error fallback blocks
├── Reporting
│   └── print_summary()          — Rich table summary
├── CLI
│   └── parse_args()             — argparse → TranslationConfig
└── Entry Point
    └── main() / asyncio.run()
```

---

## 📊 Exit Codes

| Code | Meaning |
|---|---|
| `0` | All chunks translated successfully |
| `1` | Fatal error (bad input, missing API key, I/O failure) |
| `2` | Partial success — some chunks failed after all retries |

---

## 🛠️ Troubleshooting

**`UnicodeEncodeError` in terminal**
> Run `chcp 65001` in your Windows terminal before running the script, or set `$env:PYTHONUTF8=1`.

**`RateLimitError` — too many retries**
> Lower `--concurrency` (e.g. `-c 2`) or increase `--max-retries`.

**Chunks too large / translation quality**
> Lower `--max-tokens` (e.g. `--max-tokens 800`) for better focus per translation call.

**Use a different model**
> `--model gpt-4o-mini` for cost savings, or any OpenAI-compatible model ID.
