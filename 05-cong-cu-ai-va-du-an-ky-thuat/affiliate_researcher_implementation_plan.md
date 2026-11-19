# Affiliate Competitor Research Tool

## Mục tiêu

Xây dựng một **Python script + AI** để nghiên cứu và phân tích đối thủ affiliate trên mạng xã hội Việt Nam (Instagram, Facebook, Threads, YouTube). Script chạy nội bộ trên máy, dùng AI phân tích, xuất báo cáo 3 dạng: hiển thị terminal + file Markdown + file CSV.

---

## Tổng quan giải pháp

```
Bạn nhập từ khóa / tên tài khoản
        ↓
Script tìm kiếm & scrape public data
        ↓
Gemini AI phân tích content strategy, affiliate pattern, growth
        ↓
Xuất báo cáo: terminal | report.md | data.csv
```

---

## Thông tin đã thu thập

| Hạng mục | Lựa chọn |
|---|---|
| Mục tiêu | Phân tích toàn diện: content, growth, affiliate links, sản phẩm |
| Ngành | Chưa chọn – công cụ sẽ giúp tìm & khám phá ngành phù hợp |
| Thị trường | Việt Nam – nội dung Tiếng Việt |
| Nền tảng | Instagram, Facebook, Threads, YouTube (cả 4) |
| Cách dùng | On-demand – tự chạy khi cần |
| Chế độ tìm | Tìm kiếm theo từ khóa → phân tích sâu từng người |
| Dạng tool | Python script + Gemini AI API |
| Đầu ra | Terminal + Markdown report + CSV |
| Lấy dữ liệu | Web scraping public data (miễn phí) |
| AI | Gemini API (miễn phí có quota) |

---

## Proposed Changes

### Component 1: Project Structure

```
C:\Users\groul\.gemini\antigravity\scratch\affiliate-researcher\
├── main.py                  # CLI entry point
├── config.py                # Cấu hình API key, settings
├── requirements.txt
├── scrapers/
│   ├── youtube_scraper.py   # YouTube public data (+ YouTube Data API v3 miễn phí)
│   ├── instagram_scraper.py # Instagram public profile scraping
│   ├── facebook_scraper.py  # Facebook public page scraping
│   └── threads_scraper.py   # Threads public profile scraping
├── analyzer/
│   └── ai_analyzer.py       # Gọi Gemini API phân tích
├── reporter/
│   ├── markdown_reporter.py # Xuất file .md
│   ├── csv_reporter.py      # Xuất file .csv
│   └── terminal_reporter.py # Hiển thị đẹp trên terminal
└── reports/                 # Thư mục lưu báo cáo
```

---

### Component 2: Tính năng chính

#### Chế độ 1: Tìm kiếm từ khóa
```bash
python main.py search "affiliate review sản phẩm Việt" --platform all --top 10
```
→ Tìm top 10 creator VN đang làm affiliate theo từ khóa

#### Chế độ 2: Phân tích sâu một tài khoản
```bash
python main.py analyze --instagram "@tenuser" --youtube "channel_name" 
```
→ Phân tích toàn bộ: content strategy, posting frequency, affiliate patterns

#### Báo cáo xuất ra

**Terminal** (rich formatting):
```
━━━ PHÂN TÍCH ĐỐI THỦ: @tenuser ━━━
📊 Followers: 125K | Engagement: 4.2%
📅 Tần suất: 4 bài/tuần
🎯 Content: 60% review, 30% lifestyle, 10% tips
🛍️  Affiliate: Shopee, Lazada – Ngành: làm đẹp
💡 AI nhận xét: [Phân tích chiến lược...]
```

**Markdown report** (`reports/2026-09-04_tenuser.md`)

**CSV** (`reports/data.csv`) – dễ so sánh nhiều đối thủ

---

### Component 3: AI Analysis (Gemini)

Gemini sẽ phân tích và đưa ra:
- **Content strategy**: loại nội dung nào hiệu quả nhất
- **Affiliate pattern**: cách họ chèn link, kêu gọi mua hàng tự nhiên
- **Posting formula**: giờ đăng, tần suất, format tốt nhất
- **Gap analysis**: điểm yếu của đối thủ → cơ hội cho bạn
- **Học được gì**: 3-5 điều bạn có thể áp dụng ngay

---

### Component 4: Lấy dữ liệu

| Nền tảng | Phương pháp | Dữ liệu lấy được |
|---|---|---|
| **YouTube** | YouTube Data API v3 (miễn phí 10K quota/ngày) | Video, views, likes, description, tags |
| **Instagram** | Scrape trang public (không cần login) | Bio, follower count, số bài, recent posts |
| **Facebook** | Scrape public page | Page info, bài đăng public, reactions |
| **Threads** | Scrape public profile | Bio, số bài, nội dung recent posts |

> [!IMPORTANT]
> Scraping chỉ lấy dữ liệu **public** (không cần đăng nhập). Không vi phạm Terms of Service với dữ liệu cá nhân. Tuy nhiên Instagram/Facebook có thể cần User-Agent rotation để tránh block.

---

## User Review Required

> [!WARNING]
> **YouTube Data API Key**: Đây là API duy nhất cần key, nhưng hoàn toàn **miễn phí** (Google Cloud). Tôi sẽ hướng dẫn bạn lấy key trong ~5 phút sau khi bắt đầu build.

> [!IMPORTANT]
> **Gemini API Key**: Cần để AI phân tích. Miễn phí tại [aistudio.google.com](https://aistudio.google.com). Tôi sẽ hướng dẫn cụ thể.

> [!NOTE]
> Instagram và Facebook có anti-scraping mạnh. Công cụ sẽ dùng kỹ thuật scraping nhẹ nhàng để giảm nguy cơ bị block. Trong trường hợp xấu nhất, có thể cần nhập dữ liệu thủ công cho 2 nền tảng này.

---

## Verification Plan

### Automated Tests
- Chạy `python main.py search "review sản phẩm" --platform youtube --top 5` để test tìm kiếm
- Chạy `python main.py analyze --youtube "UC..."` với một channel YouTube công khai để test phân tích đầy đủ

### Manual Verification
- Kiểm tra file `reports/` có tạo được Markdown và CSV không
- Đọc báo cáo AI và đánh giá chất lượng phân tích có hữu ích không
