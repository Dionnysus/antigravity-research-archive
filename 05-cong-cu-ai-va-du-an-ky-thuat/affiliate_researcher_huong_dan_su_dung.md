# 🔍 Affiliate Competitor Research Tool
## Hướng Dẫn Sử Dụng

Công cụ nghiên cứu đối thủ affiliate trên mạng xã hội, hỗ trợ AI phân tích chiến lược.

> [!NOTE]
> File gốc nằm tại [README.md](file:///C:/Users/groul/.gemini/antigravity/scratch/affiliate-researcher/README.md) trong thư mục dự án.

---

## Mục Lục

1. [Giới thiệu](#-giới-thiệu)
2. [Yêu cầu hệ thống](#-yêu-cầu-hệ-thống)
3. [Cài đặt](#-cài-đặt)
4. [Cấu hình API Keys](#-cấu-hình-api-keys)
5. [3 Lệnh chính](#-3-lệnh-chính)
6. [Nền tảng hỗ trợ](#-nền-tảng-hỗ-trợ)
7. [Đầu ra & Báo cáo](#-đầu-ra--báo-cáo)
8. [Ví dụ thực tế](#-ví-dụ-thực-tế)
9. [Câu hỏi thường gặp](#-câu-hỏi-thường-gặp)
10. [Xử lý lỗi](#-xử-lý-lỗi)

---

## 📖 Giới Thiệu

**Affiliate Competitor Research Tool** giúp bạn:

- 🔍 **Tìm kiếm** các creator/influencer đang làm affiliate trên mạng xã hội
- 📊 **Phân tích** chiến lược nội dung, tần suất đăng bài, engagement rate
- 🛍️ **Phát hiện** link affiliate, sản phẩm họ đang promote
- 🤖 **AI đánh giá** điểm mạnh, điểm yếu, cơ hội và gợi ý chiến lược cho bạn
- 🔄 **So sánh** nhiều đối thủ để tìm ra best practices

---

## 💻 Yêu Cầu Hệ Thống

| Yêu cầu | Phiên bản |
|---|---|
| Python | 3.10 trở lên |
| Hệ điều hành | Windows / macOS / Linux |
| Kết nối Internet | Cần thiết (để scrape và gọi AI) |

---

## 📦 Cài Đặt

### Bước 1: Mở PowerShell và vào thư mục dự án

```powershell
cd C:\Users\groul\.gemini\antigravity\scratch\affiliate-researcher
```

### Bước 2: Cài đặt thư viện (chỉ cần chạy 1 lần)

```powershell
pip install -r requirements.txt
pip install google-genai
```

### Bước 3: Kiểm tra cài đặt

```powershell
python main.py --help
```

Nếu thấy menu hiển thị các lệnh `search`, `analyze`, `compare` → **cài đặt thành công!**

---

## 🔑 Cấu Hình API Keys

> [!IMPORTANT]
> **Không có API key vẫn dùng được!** Tool sẽ tự động dùng web scraping. Tuy nhiên có API key sẽ cho kết quả chi tiết và chính xác hơn.

### API Key 1: Gemini (AI phân tích – MIỄN PHÍ)

Gemini AI giúp phân tích chiến lược, đưa ra nhận xét và gợi ý.

**Cách lấy:**

1. Truy cập 👉 https://aistudio.google.com/app/apikey
2. Đăng nhập bằng tài khoản Google
3. Nhấn **"Create API Key"**
4. Copy key (dạng `AIza...`)
5. Cấu hình trong PowerShell:

```powershell
# Cách 1: Thiết lập tạm thời (mất khi đóng PowerShell)
$env:GEMINI_API_KEY='AIzaSyxxxxxxxxxxxxxxxxxxxxxxxxx'

# Cách 2: Thiết lập vĩnh viễn
[System.Environment]::SetEnvironmentVariable('GEMINI_API_KEY', 'AIzaSyxxxxxxxxxxxxxxxxxxxxxxxxx', 'User')
```

### API Key 2: YouTube Data API v3 (dữ liệu YouTube – MIỄN PHÍ)

Cho phép lấy dữ liệu YouTube chi tiết hơn (subscriber count, video stats...).

**Cách lấy:**

1. Truy cập 👉 https://console.cloud.google.com
2. Tạo project mới (hoặc chọn project có sẵn)
3. Vào **APIs & Services** → **Library**
4. Tìm **"YouTube Data API v3"** → Nhấn **Enable**
5. Vào **Credentials** → **Create Credentials** → **API Key**
6. Copy key và cấu hình:

```powershell
# Tạm thời
$env:YOUTUBE_API_KEY='AIzaSyxxxxxxxxxxxxxxxxxxxxxxxxx'

# Vĩnh viễn
[System.Environment]::SetEnvironmentVariable('YOUTUBE_API_KEY', 'AIzaSyxxxxxxxxxxxxxxxxxxxxxxxxx', 'User')
```

---

## 🚀 3 Lệnh Chính

### 1. `search` – Tìm Kiếm Đối Thủ

Tìm kiếm creator/channel theo từ khóa trên các nền tảng.

**Cú pháp:**
```
python main.py search "từ khóa" [--platform NỀN_TẢNG] [--top SỐ_KẾT_QUẢ]
```

**Tham số:**

| Tham số | Viết tắt | Mặc định | Mô tả |
|---|---|---|---|
| `"từ khóa"` | – | *bắt buộc* | Từ khóa tìm kiếm |
| `--platform` | `-p` | `all` | Nền tảng: `youtube`, `instagram`, `facebook`, `threads`, `all` |
| `--top` | `-t` | `10` | Số kết quả tối đa |

**Ví dụ:**

```powershell
# Tìm trên tất cả nền tảng
python main.py search "review mỹ phẩm" --platform all --top 10

# Chỉ tìm trên YouTube, lấy 5 kết quả
python main.py search "review điện thoại" -p youtube -t 5

# Tìm trên Instagram
python main.py search "affiliate shopee" -p instagram
```

**Kết quả:**
- Hiển thị bảng kết quả trên terminal
- Lưu file CSV vào `reports/`
- Lưu file Markdown vào `reports/`
- Nếu có Gemini API → AI gợi ý ngách tiềm năng

---

### 2. `analyze` – Phân Tích Sâu

Phân tích chi tiết một hoặc nhiều tài khoản cụ thể.

**Cú pháp:**
```
python main.py analyze [--youtube ID] [--instagram USER] [--facebook URL] [--threads USER]
```

**Tham số:**

| Tham số | Viết tắt | Mô tả |
|---|---|---|
| `--youtube` | `-yt` | YouTube Channel ID (vd: `UCxxxxxx`) |
| `--instagram` | `-ig` | Instagram username (vd: `tenuser`) |
| `--facebook` | `-fb` | Facebook page URL (vd: `https://facebook.com/pagename`) |
| `--threads` | `-th` | Threads username (vd: `tenuser`) |

> [!TIP]
> **Cách lấy YouTube Channel ID:**
> 1. Vào kênh YouTube muốn phân tích
> 2. Nhìn trên thanh URL, sẽ thấy dạng: `youtube.com/channel/UCxxxxxxxxx`
> 3. Copy phần `UCxxxxxxxxx` – đó là Channel ID

**Ví dụ:**

```powershell
# Phân tích 1 kênh YouTube
python main.py analyze --youtube "UCxxxxxxxxxxxxxxxxxx"

# Phân tích Instagram
python main.py analyze --instagram "tenuser"

# Phân tích nhiều nền tảng cùng lúc
python main.py analyze --youtube "UCxxx" --instagram "tenuser" --threads "tenuser"
```

**Kết quả:**
- Thông tin profile (followers, bio, engagement rate...)
- Danh sách bài đăng gần đây
- Phát hiện link affiliate
- **AI phân tích** (nếu có Gemini key): chiến lược, điểm mạnh/yếu, bài học, gợi ý ngách
- Báo cáo Markdown + CSV

---

### 3. `compare` – So Sánh Đối Thủ

So sánh nhiều đối thủ trên cùng hoặc khác nền tảng.

**Cú pháp:**
```
python main.py compare [--youtube "ID1,ID2,ID3"] [--instagram "user1,user2"]
```

> [!WARNING]
> Nhiều tài khoản trên cùng nền tảng thì **cách nhau bằng dấu phẩy**, bọc trong dấu ngoặc kép.

**Ví dụ:**

```powershell
# So sánh 3 kênh YouTube
python main.py compare --youtube "UC1xxx,UC2xxx,UC3xxx"

# So sánh Instagram
python main.py compare --instagram "user1,user2,user3"

# So sánh cross-platform
python main.py compare --youtube "UCxxx" --instagram "user1,user2"
```

**Kết quả:**
- Thu thập dữ liệu từng đối thủ
- **AI so sánh**: bảng so sánh, best practices, đề xuất chiến lược
- Báo cáo so sánh Markdown + CSV

---

## 🌐 Nền Tảng Hỗ Trợ

| Nền tảng | Cách lấy dữ liệu | Mức độ chi tiết | Ghi chú |
|---|---|---|---|
| **YouTube** | YouTube API v3 + Web scraping | ⭐⭐⭐⭐⭐ | Tốt nhất, có API miễn phí |
| **Instagram** | Web scraping (meta tags) | ⭐⭐⭐ | Anti-scraping mạnh, dữ liệu hạn chế |
| **Facebook** | Web scraping (mobile fallback) | ⭐⭐ | Anti-scraping rất mạnh |
| **Threads** | Web scraping | ⭐⭐⭐ | Nền tảng mới, ít anti-scraping |

> [!TIP]
> **Khuyến nghị:** Bắt đầu với **YouTube** vì cho dữ liệu chi tiết nhất, sau đó mở rộng sang các nền tảng khác.

---

## 📁 Đầu Ra & Báo Cáo

Mọi báo cáo được lưu tự động vào thư mục `reports/`.

| Loại | Tên file | Mô tả |
|---|---|---|
| **Markdown** | `20260904_YouTube_tenuser.md` | Báo cáo đọc được, copy vào Notion/Obsidian |
| **CSV** | `20260904_youtube_tenuser_profile.csv` | Dữ liệu dạng bảng, mở bằng Excel |
| **CSV so sánh** | `comparison.csv` | Tích lũy dữ liệu qua nhiều lần analyze |

---

## 🎯 Ví Dụ Thực Tế

### Kịch bản 1: Mới bắt đầu – Tìm ngách phù hợp

```powershell
# Bước 1: Cấu hình Gemini key
$env:GEMINI_API_KEY='AIzaSyxxxxxxxxx'

# Bước 2: Tìm kiếm rộng
python main.py search "affiliate marketing Việt Nam" -p youtube -t 10

# Bước 3: Xem AI gợi ý ngách ở cuối kết quả
```

### Kịch bản 2: Đã có ngách – Nghiên cứu đối thủ

```powershell
# Bước 1: Tìm đối thủ trong ngách
python main.py search "review mỹ phẩm Việt" -p youtube -t 10

# Bước 2: Chọn 2-3 kênh hay nhất, phân tích sâu
python main.py analyze --youtube "UCxxxxxxx"

# Bước 3: Đọc báo cáo AI → rút ra bài học
```

### Kịch bản 3: So sánh nhiều đối thủ

```powershell
# So sánh tổng thể
python main.py compare --youtube "UC1xxx,UC2xxx,UC3xxx"

# Mở reports/comparison.csv bằng Excel để so sánh số liệu
explorer reports
```

### Kịch bản 4: Phân tích cross-platform

```powershell
# Phân tích 1 người trên nhiều nền tảng
python main.py analyze --youtube "UCxxx" --instagram "tenuser" --threads "tenuser"
```

---

## ❓ Câu Hỏi Thường Gặp

**Q: Không có API key thì dùng được không?**
A: Được! Nhưng không có Gemini key thì không có AI phân tích, không có YouTube key thì ít dữ liệu hơn.

**Q: Tại sao Instagram/Facebook ít dữ liệu?**
A: Anti-scraping mạnh. Tool lấy được bio, follower count, tên từ meta tags. Bài đăng thường bị chặn.

**Q: Có bị chặn IP không?**
A: Tool dùng User-Agent rotation + delay 2s. Nhưng scrape quá nhiều có thể bị tạm chặn.

**Q: YouTube Channel ID ở đâu?**
A: Từ URL `youtube.com/channel/UCxxxxxxxxx` → copy phần `UCxxxxxxxxx`.

**Q: Gemini API có giới hạn không?**
A: Gói miễn phí: 15 request/phút, 1,500 request/ngày – đủ cho nghiên cứu cá nhân.

---

## 🔧 Xử Lý Lỗi

| Lỗi | Giải pháp |
|---|---|
| GEMINI_API_KEY chưa thiết lập | `$env:GEMINI_API_KEY='your_key'` |
| Lỗi encoding/Unicode | `chcp 65001` rồi chạy lại |
| ModuleNotFoundError | `pip install -r requirements.txt` |
| 429 Too Many Requests | Tool tự chờ 60s. Nếu vẫn lỗi, đợi vài phút |
| Instagram/Facebook trống | Hạn chế scraping, thử lại sau hoặc dùng YouTube |

---

## 📋 Tham Khảo Nhanh

```powershell
# ===== TÌM KIẾM =====
python main.py search "từ khóa"                           # Tìm tất cả nền tảng
python main.py search "từ khóa" -p youtube                 # Chỉ YouTube
python main.py search "từ khóa" -p instagram -t 5          # Instagram, top 5

# ===== PHÂN TÍCH =====
python main.py analyze --youtube "UCxxx"                   # 1 kênh YouTube
python main.py analyze -ig "tenuser"                       # Instagram
python main.py analyze -yt "UCxxx" -ig "user" -th "user"   # Nhiều nền tảng

# ===== SO SÁNH =====
python main.py compare --youtube "UC1,UC2,UC3"             # So sánh YouTube
python main.py compare -ig "user1,user2" -yt "UCxxx"       # Cross-platform

# ===== TRỢ GIÚP =====
python main.py --help                                      # Menu chính
python main.py search --help                               # Help cho search
```
