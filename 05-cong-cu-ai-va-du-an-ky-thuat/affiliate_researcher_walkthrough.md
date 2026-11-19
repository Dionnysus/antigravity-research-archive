# Affiliate Competitor Research Tool – Walkthrough

## Tổng quan

Đã build xong công cụ nghiên cứu đối thủ affiliate trên 4 nền tảng mạng xã hội. Công cụ chạy bằng Python trên máy tính, sử dụng AI phân tích chiến lược.

**Thư mục dự án**: [`affiliate-researcher`](file:///C:/Users/groul/.gemini/antigravity/scratch/affiliate-researcher)

---

## Cấu trúc file đã tạo

```
affiliate-researcher/
├── main.py                     ← CLI chính (3 lệnh: search, analyze, compare)
├── config.py                   ← Cấu hình API keys & settings
├── requirements.txt            ← Thư viện cần thiết
├── scrapers/
│   ├── youtube_scraper.py      ← YouTube Data API v3 + fallback scraping
│   ├── instagram_scraper.py    ← Instagram public profile scraping
│   ├── facebook_scraper.py     ← Facebook public page scraping
│   └── threads_scraper.py      ← Threads public profile scraping
├── analyzer/
│   └── ai_analyzer.py          ← Gemini AI phân tích chiến lược (google-genai SDK)
├── reporter/
│   ├── terminal_reporter.py    ← Rich terminal output (bảng đẹp)
│   ├── markdown_reporter.py    ← Xuất file .md
│   └── csv_reporter.py         ← Xuất file .csv
└── reports/                    ← Thư mục lưu báo cáo
```

---

## Cách sử dụng

### 1. Tìm kiếm creator theo từ khóa

```powershell
cd C:\Users\groul\.gemini\antigravity\scratch\affiliate-researcher

# Tìm trên tất cả nền tảng
python main.py search "review sản phẩm" --platform all --top 10

# Chỉ tìm trên YouTube
python main.py search "affiliate marketing Việt" --platform youtube --top 5

# Chỉ tìm trên Instagram
python main.py search "review mỹ phẩm" --platform instagram
```

### 2. Phân tích sâu một tài khoản

```powershell
# Phân tích YouTube channel
python main.py analyze --youtube "UC_channel_id"

# Phân tích nhiều nền tảng cùng lúc
python main.py analyze --youtube "UC..." --instagram "tenuser"

# Phân tích Facebook page
python main.py analyze --facebook "https://facebook.com/pagename"
```

### 3. So sánh nhiều đối thủ

```powershell
# So sánh 3 kênh YouTube
python main.py compare --youtube "UC1,UC2,UC3"

# So sánh cross-platform
python main.py compare --youtube "UC..." --instagram "user1,user2"
```

---

## Cài đặt API Keys (tùy chọn nhưng khuyến khích)

### Gemini API Key (MIỄN PHÍ – cho AI phân tích)

1. Truy cập https://aistudio.google.com/app/apikey
2. Nhấn "Create API Key"
3. Copy key và chạy:

```powershell
$env:GEMINI_API_KEY='your_key_here'
```

### YouTube Data API Key (MIỄN PHÍ – cho dữ liệu chi tiết hơn)

1. Truy cập https://console.cloud.google.com/apis/credentials
2. Tạo project mới → Enable "YouTube Data API v3"
3. Create Credentials → API Key
4. Chạy:

```powershell
$env:YOUTUBE_API_KEY='your_key_here'
```

> [!TIP]
> Không có API key vẫn dùng được! Tool sẽ fallback sang web scraping. Tuy nhiên có key sẽ cho kết quả chi tiết và chính xác hơn nhiều.

---

## Kết quả test

| Test | Kết quả |
|------|---------|
| `python main.py --help` | ✅ Hiển thị menu đẹp |
| `python main.py` | ✅ Hướng dẫn nhanh |
| `python main.py search "review san pham" --platform youtube --top 3` | ✅ Tìm được 3 kết quả, lưu CSV + MD |

---

## Sửa lỗi đã thực hiện

1. **Deprecated SDK**: Chuyển từ `google.generativeai` (deprecated) sang `google.genai` (mới nhất)
2. **Windows encoding**: Thêm UTF-8 encoding wrapper để hỗ trợ emoji + tiếng Việt trên Windows
3. **Import path**: Sửa `from utils import config` → `import config`
