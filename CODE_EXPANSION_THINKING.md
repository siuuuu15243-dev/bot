# TƯ DUY LẬP TRÌNH MỞ RỘNG (EXPANSIVE CODING THINKING)

Bên cạnh tư duy logic nhanh và trực diện (Logic Thinking), **Tư duy mở rộng (Expansive Thinking)** giúp AI và Lập trình viên thiết kế những hệ thống có khả năng mở rộng tốt, linh hoạt trước thay đổi, dễ bảo trì và có tính tái sử dụng cao mà không biến code thành "đá tảng" phức tạp quá mức (over-engineering).

---

## 1. Thiết kế Hướng Tương Lai (Design for the Future, Code for the Present)
* **Quy tắc YAGNI (You Aren't Gonna Need It):** Đừng viết code cho những tính năng "có thể cần" trong tương lai trừ khi có yêu cầu thực tế hoặc định hướng rõ ràng.
* **Cơ chế mở rộng cắm và chạy (Plug-and-Play / Open-Closed Principle):** Viết code sao cho khi cần thêm tính năng mới, bạn chỉ cần **viết thêm code mới (extension)** chứ không cần **sửa đổi code cũ (modification)**. 
  * *Cách làm:* Sử dụng Interface, Polymorphism (Đa hình), hoặc Abstract Classes.
* **Tách biệt mối quan tâm (Separation of Concerns):** Mỗi module/layer chỉ làm tốt một nhiệm vụ duy nhất. Ví dụ: Tách biệt Business Logic khỏi Data Access và UI/Presentation Layer.

---

## 2. Tư Duy Trừu Tượng Hóa Phù Hợp (Healthy Abstraction)
* **Đừng lặp lại chính mình (DRY - Don't Repeat Yourself) một cách mù quáng:** Đôi khi, việc lặp lại 2-3 dòng code đơn giản tốt hơn là tạo ra một hàm trừu tượng hóa quá phức tạp, khó đọc và khó gỡ lỗi (gọi là *Abuse of Abstraction*).
* **Tư duy hướng cấu hình (Config-Driven Development):** Tránh "hard-code" các hằng số, API key, đường dẫn hoặc logic cấu hình động. Hãy đưa chúng ra file cấu hình (`.env`, `config.json`, v.v.) để hệ thống linh hoạt chuyển đổi môi trường (Development, Staging, Production).

---

## 3. Tư Duy Phòng Thủ & Xử Lý Sự Cố (Defensive & Resilient Thinking)
* **Xác thực dữ liệu từ ranh giới (Edge Input Validation):** Luôn coi mọi dữ liệu đầu vào từ người dùng hoặc API bên thứ ba là không an toàn. Hãy xác thực dữ liệu ngay tại cửa ngõ đầu tiên.
* **Cơ chế chịu lỗi (Graceful Degradation / Fault Tolerance):**
  * Thiết lập cơ chế Timeout hợp lý cho mọi truy vấn I/O hoặc API ngoại vi.
  * Triển khai Retry Pattern khi gọi dịch vụ ngoài (với thuật toán Exponential Backoff để tránh làm sập hệ thống nguồn).
  * Dự phòng phương án fallback (ví dụ: Trả về dữ liệu cũ từ cache khi API thực bị lỗi hoặc sập).

---

## 4. Tối Ưu Hóa Hiệu Năng Tư Duy (Performance & Resource Consciousness)
* **Hiểu rõ độ phức tạp thuật toán (Time & Space Complexity - O(n)):** 
  * Cảnh giác với các vòng lặp lồng nhau (Nested Loops -> $O(n^2)$).
  * Sử dụng cấu trúc dữ liệu phù hợp (Ví dụ: Tra cứu nhanh bằng `Set` hoặc `Map`/`Hash Table` thay vì duyệt qua `Array` từ đầu đến cuối).
* **Tránh rò rỉ tài nguyên (Resource Leakage):** Luôn giải phóng tài nguyên sau khi sử dụng (đóng database connection, close stream, dọn dẹp event listeners).

---

## 5. Tư duy Viết Code "Tự giải thích" (Self-Documenting Code)
* **Đặt tên có nghĩa (Expressive Naming):** Tên biến, tên hàm phải thể hiện rõ **ý định (intent)** chứ không chỉ là hành động thô.
  * *Ví dụ:* `isUserActive()` thay vì `checkStatus()`.
* **Viết "Tại sao" chứ không viết "Thế nào" trong Comment:** Code chỉ ra *Làm thế nào* chương trình chạy. Comment nên được dùng để giải thích *Tại sao* chúng ta lại chọn giải pháp đó (đặc biệt khi giải pháp có vẻ bất thường hoặc giải quyết một trường hợp biên cụ thể).

---

## 🛠 CHECKLIST MỞ RỘNG TRƯỚC KHI REFACTOR CODE
* [ ] **Khả dụng (Portability):** Code này có dễ dàng di chuyển hay tái sử dụng ở dự án khác không?
* [ ] **Bảo trì (Maintainability):** Người mới đọc vào có hiểu được luồng xử lý trong vòng 3 phút không?
* [ ] **Khả thử nghiệm (Testability):** Logic này có dễ dàng viết Unit Test độc lập mà không cần khởi tạo quá nhiều mock phức tạp không?
* [ ] **Sự phụ thuộc (Dependency):** Module này có đang bị liên kết quá chặt chẽ (tightly coupled) vào các module khác không? Nếu có, hãy tìm cách tách chúng ra (decouple).
