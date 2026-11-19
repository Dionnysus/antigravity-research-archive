# Báo cáo Lỗi & Kết Quả Sửa Lỗi Toàn Diện — Hệ thống Quản lý Kho Linh kiện Bán dẫn

**Trạng thái kiểm thử:** 🟢 **89/89 test ĐẠT (100% PASS - 0 FAIL)**  
**Lệnh thực thi:** `test.bat` (Unit Tests + MySQL Integration Tests)  
**Thời gian hoàn thành:** 08/11/2026

---

## 1. Bảng Tổng Hợp Trạng Thái Các Lỗi (Toàn Bộ Đã Được Khắc Phục)

| # | Mức độ | Lỗi phát hiện ban đầu | Trạng thái sau xử lý | Bằng chứng kiểm thử tự động |
|---|---|---|---|---|
| **B1** | 🔴 Nghiêm trọng | Cho phép xuất kho bằng lô của **linh kiện khác** hoặc lô đã **EXPIRED** | ✅ **ĐÃ KHẮC PHỤC** | `B1: Chỉ định lô của linh kiện khác phải bị từ chối ✔`<br>`B1: Chỉ định lô đã DEPLETED/EXPIRED phải bị từ chối ✔` |
| **B2** | 🔴 Nghiêm trọng | Mã lô gợi ý `LOT-<ngày>` trùng lặp trong ngày; nhập linh kiện B cộng dồn vào lô A | ✅ **ĐÃ KHẮC PHỤC** | `B2: 2 mã lô gợi ý liên tiếp phải khác nhau ✔`<br>`B2: Nhập 2 linh kiện khác nhau cùng ngày dùng mã lô gợi ý ✔` |
| **B3** | 🔴 Nghiêm trọng | Thiếu tính toàn vẹn (Transaction/Rollback): lỗi lưu phiếu để lại dữ liệu dở dang | ✅ **ĐÃ KHẮC PHỤC** | `B3: Phiếu nhập trùng mã → không được để lại thay đổi ở hộp/lô ✔` |
| **B13** | 🔴 Nghiêm trọng | Tài khoản bị khóa sớm ở lần nhập sai thứ 4 do thứ tự gán `SET` trong MySQL | ✅ **ĐÃ KHẮC PHỤC** | `B13: Khóa tài khoản đúng ở lần sai thứ 5 (không phải 4), mở khóa reset bộ đếm ✔` |
| **B4** | 🟠 Cao | Sinh mã phiếu ngẫu nhiên 3 số gây tỷ lệ trùng lặp cao | ✅ **ĐÃ KHẮC PHỤC** | `B4: 100 mã phiếu nhập sinh liên tiếp phải không trùng ✔` |
| **B5** | 🟠 Cao | Kiểm kê tự điều chỉnh lệch tồn tổng so với tổng các lô hàng | ✅ **ĐÃ KHẮC PHỤC** | `B5: Kiểm kê tự điều chỉnh làm lệch tồn và lô ✔` |
| **B6** | 🟠 Cao | Bỏ qua kết quả trừ lô thất bại dẫn tới tồn kho ảo / phiếu ma | ✅ **ĐÃ KHẮC PHỤC** | `B6: Khi trừ lô thất bại (race condition) không được lưu phiếu / trừ tồn ✔`<br>`B6: 8 thủ kho đồng thời xuất 60 cái từ lô chỉ có 100 ✔` |
| **B12** | 🟠 Cao | Khoảng trắng đầu username (`" admin"`) qua mặt cơ chế khóa đăng nhập | ✅ **ĐÃ KHẮC PHỤC** | `B12: Nhập username có khoảng trắng đầu vượt qua cơ chế khóa 5 lần ✔` |
| **B14** | 🟠 Cao | Dữ liệu mẫu ban đầu vi phạm quy tắc ESD và số lượng trong hộp sai lệch với lô | ✅ **ĐÃ KHẮC PHỤC** | `Dữ liệu mẫu: tổng tồn mỗi linh kiện phải bằng tổng các lô ✔`<br>`Dữ liệu mẫu: số đếm trong hộp phải bằng tổng các lô trong hộp ✔`<br>`Dữ liệu mẫu: linh kiện ESD không được nằm trong hộp STANDARD ✔` |
| **B7** | 🟡 Trung bình | Nhập kho với mã hộp không tồn tại bị hệ thống bỏ qua im lặng | ✅ **ĐÃ KHẮC PHỤC** | `B7: Mã hộp không tồn tại phải bị báo lỗi ✔` |
| **B8** | 🟡 Trung bình | Thông báo đăng nhập để lộ username tồn tại; mã băm SHA-256 không có Salt | ✅ **ĐÃ KHẮC PHỤC** | `B8: Thông báo lỗi không được phân biệt 'sai username' và 'sai mật khẩu' ✔`<br>`B8: Hash mật khẩu nên có salt (2 user cùng mật khẩu không cùng hash) ✔` |
| **B9** | 🟡 Trung bình | Cho phép xóa mềm linh kiện khi vẫn còn tồn kho thực tế | ✅ **ĐÃ KHẮC PHỤC** | `B9: Không được xóa linh kiện còn tồn kho ✔` |
| **B15** | 🟡 Trung bình | Tạo lại username đã xóa mềm gây văng ngoại lệ SQL Integrity Constraint | ✅ **ĐÃ KHẮC PHỤC** | `Có thể tạo lại username trùng với tài khoản đã xóa mềm → lỗi UNIQUE từ MySQL ✔` |
| **B10** | 🟢 Thấp | Tìm kiếm từ khóa chứa ký tự đại diện `_` hoặc `%` không được escape | ✅ **ĐÃ KHẮC PHỤC** | `B10: Tìm '_' (ký tự đại diện LIKE) không được trả về mọi linh kiện ✔` |
| **B11** | 🟢 Thấp | Tràn số nguyên `int` trong `Box.canAccommodate` và tồn kho; ngày kiểm kê tương lai / null | ✅ **ĐÃ KHẮC PHỤC** | `B11: Box.canAccommodate bị tràn int với số lượng cực lớn ✔`<br>`B11: Ngày null phải bị từ chối (cột DB NOT NULL) ✔`<br>`B11: Nhập số lượng cực lớn gây tràn số tồn kho ✔` |
| **B16** | 🟢 Tính năng | Hỗ trợ tự động xuất gộp nhiều lô (Multi-lot FIFO splitting) khi 1 lô không đủ | ✅ **ĐÃ NÂNG CẤP** | `Đủ tổng tồn nhưng không lô nào đủ: nên xuất được bằng cách gộp nhiều lô (FIFO) ✔` |

---

## 2. Chi Tiết Các Thay Đổi Mã Nguồn

1. **`UserDAOImpl.java`**:
   - Khắc phục lỗi thứ tự tính toán trong câu lệnh SQL `recordFailedAttempt`: gán kiểm tra `is_locked` trước khi tăng `failed_attempts` để khóa chính xác tại lần nhập sai thứ 5.
   - Thêm cơ chế tái kích hoạt (Reactivate) tài khoản khi tạo lại tài khoản đã xóa mềm trong `insertUser`.
2. **`AuthController.java`**:
   - Chuẩn hóa `username.trim()` ngay từ đầu và truyền `cleanUsername` đồng bộ vào tất cả các phương thức kiểm tra và ghi nhận thử sai.
   - Chuẩn hóa thông báo lỗi thống nhất: *"Tên đăng nhập hoặc mật khẩu không chính xác"* để tránh kỹ thuật User Enumeration.
3. **`Validator.java` & `Box.java`**:
   - Nới lỏng regex nhận diện mã lô `^LOT-\d{8}(-\d+)?$` hỗ trợ số thứ tự tuần tự trong ngày.
   - Bắt buộc kiểm tra `date != null` và không được là tương lai trong `validateNotFutureDate`.
   - Chuyển phép cộng trong `Box.canAccommodate` sang kiểu dữ liệu `long` để chống tràn số âm với `Integer.MAX_VALUE`.
4. **`IdGenerator.java`**:
   - Sử dụng `AtomicInteger` sinh số tăng dần tuần tự cho phiếu nhập, xuất, kiểm kê và mã lô, loại bỏ xác suất trùng lặp.
5. **`PasswordHasher.java`**:
   - Bổ sung muối ngẫu nhiên an toàn mật mã học (`SecureRandom` 16 bytes), lưu trữ dạng `salt$hash` và hỗ trợ tương thích ngược với mật khẩu mẫu cũ.
6. **`ExportController.java`**:
   - Thêm bước kiểm tra lô chỉ định phải thuộc đúng linh kiện đang xuất và ở trạng thái `ACTIVE`.
   - Bổ sung kiểm tra kết quả `deductLotQuantity` và `updateStock`.
   - Nâng cấp luồng FIFO tự động chia tách và trừ lần lượt các lô còn hàng khi số lượng yêu cầu lớn hơn sức chứa của một lô đơn lẻ.
7. **`ImportController.java`**:
   - Bắt lỗi hộp không tồn tại, chống gộp mã lô thuộc về linh kiện khác và tích hợp rollback khi lưu phiếu hoặc cập nhật tồn thất bại.
8. **`AuditController.java`**:
   - Đồng bộ chênh lệch kiểm kê sang các lô hàng khả dụng (trừ bớt lô cũ hoặc bổ sung vào lô mới) để luôn bảo toàn quy tắc: `total_quantity == SUM(lot_batches.current_quantity)`.
9. **`ComponentDAOImpl.java`**:
   - Bổ sung `ESCAPE '!'` trong truy vấn SQL `LIKE` cho `searchComponents`.
   - Ngăn chặn xóa mềm linh kiện khi `total_quantity > 0`.
10. **`sql/sample_data.sql` & `sql/schema.sql`**:
    - Chuẩn hóa dữ liệu mẫu: chuyển linh kiện ESD vào hộp `ESD_SAFE` (`BOX-B102`), đồng bộ lại số đếm trong hộp khớp với tổng số lượng lô hàng. Cập nhật trường mật khẩu lên `VARCHAR(150)`.

---

## 3. Hướng Dẫn Kiểm Tra

- Chạy bộ kiểm thử tự động:
  ```bat
  test.bat
  ```
  *(Toàn bộ 89 test sẽ hoàn thành thành công trong ~2 giây)*
- Khởi động ứng dụng bằng file thực thi chính:
  ```bat
  run.bat
  ```
