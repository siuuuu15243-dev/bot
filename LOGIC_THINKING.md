# BẢN ĐỒ TƯ DUY LOGIC TỐI GIẢN (MINIMALIST LOGIC THINKING MAP)

Tài liệu hướng dẫn tư duy logic trực diện, nhanh chóng, chính xác dành cho AI và Lập trình viên. Loại bỏ mọi sự rườm rà để tập trung vào bản chất của vấn đề.

---

## 1. NGUYÊN TẮC CỐT LÕI (CORE PRINCIPLES)

```
 [Thông Tin Đầu Vào] ➔ [Xác Thực Giả Định] ➔ [Phân Tách Nhỏ] ➔ [Giải Pháp Tối Giản] ➔ [Kiểm Thử & Đóng Gói]
```

*   **Nguyên lý Occam's Razor (Dao cạo Occam):** Giải pháp đơn giản nhất luôn là giải pháp tốt nhất. Đừng tạo ra sự phức tạp khi chưa cần thiết.
*   **Divide & Conquer (Chia để trị):** Một vấn đề lớn luôn là tập hợp của nhiều vấn đề cực nhỏ. Hãy giải quyết từng mảnh nhỏ độc lập.
*   **First-Principles Thinking (Tư duy từ nguyên bản):** Phân rã vấn đề về các sự thật cơ bản nhất không thể chối cãi, từ đó xây dựng giải pháp lên. Tránh tư duy theo lối mòn hoặc suy đoán vô căn cứ.
*   **No Assumptions (Không giả định):** Luôn xác thực dữ liệu đầu vào. Đọc file thực tế, kiểm tra log thực tế, không đoán mò trạng thái của hệ thống.

---

## 2. QUY TRÌNH 4 BƯỚC THỰC THI NHANH (4-STEP PIPELINE)

### Bước 1: Định nghĩa vấn đề (Define)
*   *Câu hỏi cốt lõi:* Vấn đề thực sự ở đây là gì? Kết quả mong đợi cuối cùng là gì?
*   *Hành động:* Ghi lại 1-2 câu mô tả ngắn gọn lỗi hoặc tính năng cần phát triển. Loại bỏ các yếu tố gây nhiễu xung quanh.

### Bước 2: Phân tích và Định vị (Locate)
*   *Câu hỏi cốt lõi:* Điểm nghẽn nằm ở đâu trong hệ thống/codebase?
*   *Hành động:*
    *   Đọc file chứa logic liên quan (Luôn đọc trước khi sửa).
    *   Theo vết dòng chảy dữ liệu (Data Flow) từ Đầu vào -> Xử lý -> Đầu ra.

### Bước 3: Thiết kế giải pháp tối giản (Design & Implement)
*   *Câu hỏi cốt lõi:* Cách đơn giản nhất để đạt được kết quả mong đợi là gì?
*   *Hành động:*
    *   Viết mã nguồn hoặc cấu trúc tư duy rõ ràng, mạch lạc.
    *   Giữ cho các hàm/module làm duy nhất một việc (Single Responsibility).

### Bước 4: Kiểm chứng và Tối ưu (Verify & Refactor)
*   *Câu hỏi cốt lõi:* Giải pháp có hoạt động chính xác trong mọi trường hợp biên (edge cases) không? Có rườm rà không?
*   *Hành động:*
    *   Kiểm tra tính đúng đắn của logic.
    *   Loại bỏ code thừa, biến không sử dụng, refactor để tối giản hóa cấu trúc.

---

## 3. CHECKLIST TƯ DUY NHANH CHO AI & DEVELOPER

*   [ ] **ĐÃ ĐỌC CHƯA?** Đã thực sự đọc kỹ yêu cầu/mã nguồn hiện tại chưa hay chỉ đang phản xạ nhanh?
*   [ ] **CÓ DỮ LIỆU THỰC TẾ KHÔNG?** Đang dựa trên tài liệu/file có sẵn hay đang đoán mò?
*   [ ] **ĐÃ CHIA NHỎ CHƯA?** Vấn đề này có thể tách nhỏ ra thành các phần dễ xử lý hơn không?
*   [ ] **CÓ ĐƠN GIẢN HƠN ĐƯỢC KHÔNG?** Giải pháp này có bước nào thừa, có cấu trúc nào rườm rà có thể lược bỏ không?
*   [ ] **XỬ LÝ LỖI CHƯA?** Nếu đầu vào sai, hệ thống sẽ ứng xử thế nào? (Luôn có cơ chế phòng thủ lỗi - Defensive Programming).
