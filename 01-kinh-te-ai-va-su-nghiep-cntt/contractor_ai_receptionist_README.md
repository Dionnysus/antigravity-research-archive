# Apex Roofing & Exterior — 24/7 AI Call Rescue & Dispatch Engine

Bộ khung dự án thực chiến **"Vũ Khí Số 1"** (dành riêng cho lộ trình kiếm USD ngắn hạn trên Upwork + xây phễu B2B Affiliate tự vận hành).

Điểm đặc biệt: Toàn bộ Backend Python được thiết kế **0 phụ thuộc thư viện ngoài (Zero External Pip Dependencies)** để bạn mở máy Windows lên chạy thử thành công ngay trong **30 giây đầu tiên**, không bao giờ bị kẹt lỗi môi trường!

---

## 1. Chạy Thử Ngay Tối Nay Trên Máy Windows Của Bạn (60 Giây)

Mở PowerShell tại thư mục dự án này và chạy đúng 1 lệnh:

```powershell
python -m app.server
```

Sau đó mở trình duyệt vào địa chỉ: **`http://localhost:8080`**

* Bấm nút **`+ Simulate Emergency Leak Call`** (đỏ): Hệ thống sẽ ký chữ ký bảo mật HMAC-SHA256 giả lập một cuộc gọi Vapi.ai thật từ chủ nhà ở Austin, Texas bị dột trần phòng ngủ, tự chuẩn hóa SĐT chuẩn Mỹ (`+15125550147`), chấm điểm khẩn cấp **`CRITICAL • 100/100`**, ước tính giá trị hợp đồng **`USD 1,200 – 6,500`** và hiển thị ngay lên bảng điều phối!
* Bấm vào bất kỳ dòng khách hàng nào để mở cửa sổ xem **Transcript hội thoại Voice AI** chi tiết.
* Bấm **`+ Test SEO Spam Block`** để xem hệ thống tự động chặn cuộc gọi rác chào dịch vụ SEO và gán giá trị `USD 0`.

*(Chạy kiểm thử tự động toàn bộ logic bảo mật & chấm điểm bằng lệnh: `python -m unittest discover -s tests -v`)*

---

## 2. Bản Đồ Thư Mục Tương Ứng Với Lịch Trình 7 Buổi Tối Của Bạn

| Tệp / Thư mục | Dùng vào buổi nào? | Tác dụng thực tế |
| :--- | :--- | :--- |
| `app/server.py` & `app/static/` | **Ngay tối nay & Tối 7 (Quay Loom)** | Màn hình Command Center trực quan để bạn bật bên cạnh điện thoại khi quay video demo 90 giây tiếng Anh gửi khách Mỹ/Úc. |
| `infra/docker-compose.yml` & `infra/Caddyfile` | **Tối 2 (Đưa lên Linux VPS 5 USD)** | Chạy đồng thời **Caddy (tự xin HTTPS/SSL miễn phí)** + **`n8n` tự host (0 USD/tháng)** + **`lead-processor`** chỉ bằng 1 lệnh `docker compose up -d --build`. |
| `supabase/schema.sql` | **Tối 3 (Thiết kế SQL chuẩn)** | Paste vào SQL Editor của Supabase để tạo bảng PostgreSQL có sẵn Index, Trigger và **Row-Level Security (RLS)** chuẩn Production. |
| `prompts/roofing_receptionist_vapi.md` | **Tối 4 (Tạo Lễ tân Voice AI)** | Bộ câu chào, System Prompt tiếng Anh chuẩn từ vựng ngành Mái nhà/Xây dựng Mỹ và JSON Schema để dán vào Vapi.ai / Retell AI. |
| `app/lead_processor.py` | **Tối 5 (Backend & Bảo mật)** | Code Python xác thực chữ ký HMAC-SHA256 chống giả mạo Webhook, chuẩn hóa SĐT quốc tế E.164, lọc spam và chấm điểm khẩn cấp. |
| `n8n/contractor_voice_workflow.json` | **Tối 6 (Nối Lịch & Báo tin)** | File mẫu import thẳng vào `n8n` để nối Vapi Webhook -> Python Scorer -> Google Calendar -> Telegram/SMS chủ thầu. |
