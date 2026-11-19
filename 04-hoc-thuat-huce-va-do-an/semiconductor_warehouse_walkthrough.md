# Walkthrough — Khắc Phục Toàn Diện Lỗi & Kiểm Thử Tự Động

## 1. Kết Quả Kiểm Thử Cuối Cùng
- **Tổng số test cases:** 89
- **Kết quả:** 🟢 **89/89 ĐẠT (100% SUCCESS, 0 FAILURES)**
- **Thời gian thực thi:** ~2.3 giây
- **Môi trường xác thực:** Kiểm thử kết hợp Unit Tests (In-memory Mock DAOs) và Integration Tests (trực tiếp trên máy chủ MySQL thật).

---

## 2. Tóm Tắt Các Khắc Phục

1. **Khắc phục lỗi logic Xuất/Nhập kho (B1, B2, B3, B7, B16):**
   - Đảm bảo lô xuất bắt buộc phải thuộc linh kiện đang chọn và có trạng thái `ACTIVE`.
   - Bổ sung cơ chế xuất gộp nhiều lô (Multi-lot splitting) tự động theo thứ tự FIFO khi 1 lô không đủ số lượng.
   - Kiểm tra hộp lưu trữ tồn tại, ngăn chặn nhập mã lô trùng thuộc về linh kiện khác.
   - Thêm cơ chế hoàn tác (Rollback) thủ công bảo toàn dữ liệu giữa Hộp, Lô, Phiếu và Tồn kho khi có lỗi phát sinh giữa chừng.

2. **Khắc phục xác thực và bảo mật (B8, B12, B13, B15):**
   - Sửa thứ tự gán giá trị trong câu lệnh `UPDATE` để khóa chính xác tại lần nhập sai thứ 5.
   - Triệt tiêu lỗi khoảng trắng username bằng `trim()` đồng bộ, chống tấn công brute-force.
   - Thống nhất thông điệp đăng nhập chống User Enumeration.
   - Nâng cấp `PasswordHasher` với salt ngẫu nhiên 16 bytes (`salt$hash`) và vẫn tương thích ngược với dữ liệu cũ.
   - Hỗ trợ khôi phục/kích hoạt lại tài khoản đã xóa mềm mà không gây văng ngoại lệ SQL Unique.

3. **Toàn vẹn dữ liệu và kiểm kê (B4, B5, B6, B9, B10, B11, B14):**
   - Chuyển việc sinh ID và mã lô sang `AtomicInteger` tránh va chạm mã.
   - Đồng bộ chênh lệch kiểm kê sang các lô hàng, đảm bảo bất biến: `total_quantity == SUM(lot_batches.current_quantity)`.
   - Ngăn xóa mềm linh kiện khi tồn kho vẫn còn lớn hơn 0.
   - Escape ký tự `_` và `%` trong truy vấn tìm kiếm linh kiện.
   - Khắc phục nguy cơ tràn số âm trong `Box.canAccommodate`.
   - Chuẩn hóa toàn bộ schema và dữ liệu mẫu (`sql/sample_data.sql`).

---

## 3. Xác Minh Bản Build

- File thực thi JAR đã được cập nhật thành công:
  ```
  dist\SemiconductorWarehouse.jar
  ```
- Lệnh chạy kiểm thử: `test.bat`
- Lệnh chạy ứng dụng: `run.bat`
