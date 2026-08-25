# CẨM NANG TOÀN DIỆN VỀ ỨNG DỤNG SHOPEE & CHI TIẾT CÁC CÁCH NHẬN SHOPEE XU

## 1. TỔNG QUAN VỀ ỨNG DỤNG SHOPEE & HỆ THỐNG SHOPEE XU
Shopee là nền tảng thương mại điện tử hàng đầu tại Đông Nam Á. Ứng dụng được thiết kế theo mô hình **Gamification Shopping** (kết hợp mua sắm và giải trí), trong đó **Shopee Xu (Shopee Coins)** đóng vai trò là đơn vị điểm thưởng trung tâm để thu hút và giữ chân người dùng.

### Quy đổi và Giá trị của Shopee Xu:
- **Tỷ lệ quy đổi**: `1 Shopee Xu = 1 VNĐ`.
- **Phạm vi sử dụng**: 
  - Trừ trực tiếp vào tổng tiền thanh toán đơn hàng (tối đa theo hạn mức hệ thống quy định).
  - Quy đổi lấy Voucher giảm giá, mã miễn phí vận chuyển, hoặc quà tặng đối tác.
  - Sử dụng làm phí/lượt chơi các trò chơi trong Shopee Games.
- **Hạn sử dụng**: Shopee Xu có thời hạn sử dụng (thường là ngày cuối cùng của tháng thứ 3 kể từ ngày nhận).

---

## 2. BỐ CỤC, THIẾT KẾ VÀ PHÂN BỐ GIAO DIỆN SHOPEE (LAYOUT & UI DESIGN)

Ứng dụng Shopee được chia thành các khu vực bố cục chính:

```text
+-------------------------------------------------------------+
| [HEADER] Thanh Tìm kiếm | Giỏ hàng | Chat (Shopee Chat)    |
+-------------------------------------------------------------+
| [BANNER] Slide Quảng cáo & Sự kiện Nổi bật                 |
+-------------------------------------------------------------+
| [QUICK ACCESS ICON GRID]                                    |
| [Khung Giờ Săn Sale] [Shopee Xu] [Shopee Game] [Voucher]   |
+-------------------------------------------------------------+
| [MAIN CONTENT AREA]                                         |
| - Flash Sale / Shopee Live / Shopee Video                   |
| - Gợi ý Hôm Nay (Personalized Recommendation Feed)          |
+-------------------------------------------------------------+
| [NAVIGATION BAR (BOTTOM)]                                   |
| [Trang chủ] [Shopee Live] [Shopee Video] [Thông báo] [Tôi] |
+-------------------------------------------------------------+
```

### Chi tiết phân bố các nút/mục liên quan đến Shopee Xu:
1. **Trang Chủ (Home Tab)**:
   - Dynamic Grid Icon: Nút **"Săn Xu"** hoặc **"Shopee Xu"** (biểu tượng đồng xu vàng).
   - Biểu tượng **"Shopee Game"** / **"Nông Trại Shopee"**.
2. **Tab Shopee Live**:
   - Icon xem livestream nhận xu (thường có biểu tượng Túi Xu hoặc Lì Xì góc trên màn hình live).
3. **Tab Shopee Video**:
   - Vòng tròn tiến trình thưởng xu (Coin Progress Ring) ở góc màn hình.
4. **Tab Tôi (Account Tab)**:
   - Mục **"Shopee Xu"**: Hiển thị tổng số xu hiện có, lịch sử cộng/trừ xu và hạn sử dụng.
   - Mục **"Đơn Mua"** -> **"Đã Giao"**: Nút Đánh giá sản phẩm nhận xu.

---

## 3. THAO TÁC CHI TIẾT TẤT CẢ CÁC CÁCH NHẬN SHOPEE XU

### 3.1. Điểm Danh Hàng Ngày (Daily Check-in)
- **Vị trí**: Trang chủ -> Icon **"Shopee Xu"** (hoặc tab **Tôi** -> **Shopee Xu**).
- **Cách thao tác**:
  1. Mở ứng dụng Shopee.
  2. Nhấp vào icon **"Shopee Xu"** hoặc biểu tượng **Săn Xu**.
  3. Bấm vào nút **"Nhấn để nhận xu"** (hoặc số xu tương ứng ngày đó).
  4. Duy trì chuỗi điểm danh 7 ngày liên tiếp để nhận mức xu thưởng tăng dần và xu bonus ngày thứ 7.

---

### 3.2. Chơi Shopee Games (Hệ Thống Giải Trí Tích Xu)

Shopee tích hợp nhiều mini-game giải trí cho phép tích lũy xu hàng ngày:

#### A. Nông Trại Shopee (Shopee Farm)
- **Cách thao tác**:
  1. Vào mục **Shopee Game** -> Chọn **Nông Trại Shopee**.
  2. Chọn trồng cây mầm **Xu** (Cây Shopee Xu).
  3. Thực hiện thao tác **Tưới nước** bằng cách tích lũy giọt nước (từ điểm danh, điểm danh bạn bè, mua hàng, xem clip).
  4. Khi cây thu hoạch, bấm **Thu hoạch** để nhận trực tiếp Shopee Xu vào ví.

#### B. Shopee Đập Kẹo / Shopee Bắn Bong Bóng / Shopee Máy Gắp Xu
- **Cách thao tác**:
  1. Vào **Shopee Game** -> Chọn game tương ứng.
  2. Vượt qua các màn chơi (Levels) hoặc dùng lượt chơi miễn phí mỗi ngày.
  3. Đạt mốc điểm quy định hoặc gắp trúng hộp quà chứa Xu.
  4. Đổi điểm/kim cương trong game ra Shopee Xu tại Cửa hàng đổi quà của Game.

#### C. Vòng Quay May Mắn (Lucky Spin)
- **Cách thao tác**: Vào mục Game -> Chọn **Vòng Quay May Mắn** -> Bấm **Quay**. Mỗi ngày được tặng lượt quay miễn phí để trúng xu hoặc voucher hoàn xu.

---

### 3.3. Xem Shopee Live (Livestream Nhận Xu)
- **Vị trí**: Tab **Shopee Live** thanh menu dưới cùng.
- **Dấu hiệu nhận biết Livestream có xu**: Có nhãn biểu tượng **"Túi Xu"** hoặc chữ **"Thưởng Xu"** hiển thị ngoài ảnh thumbnail của Livestream.
- **Cách thao tác**:
  1. Chọn và vào xem một Livestream có gắn nhãn nhận xu.
  2. Chờ đồng hồ đếm ngược (thường là 3 phút, 5 phút, 10 phút) ở biểu tượng túi xu góc màn hình.
  3. Khi đồng hồ đếm ngược về `00:00`, túi xu chuyển sang trạng thái nhấp nháy/sẵn sàng.
  4. Bấm thật nhanh vào **"Nhận ngay"** / **"Lấy xu"** trước khi số lượng xu trong phiên hết lượt.
  5. Tiếp tục ở lại livestream để chờ phiên đếm ngược tiếp theo.

---

### 3.4. Xem Shopee Video (Lướt Clip Nhận Xu)
- **Vị trí**: Tab **Shopee Video** ở thanh menu bên dưới.
- **Cách thao tác**:
  1. Nhấp vào tab **Shopee Video**.
  2. Quan sát biểu tượng **Vòng Tròn Thưởng Xu** ở góc màn hình.
  3. Lướt xem các video ngắn. Khi xem, thanh tiến trình màu vàng sẽ tự động chạy.
  4. Khi thanh tiến trình đầy 1 vòng, hệ thống tự động cộng Shopee Xu (hoặc người dùng bấm vào biểu tượng để nhận xu thưởng).
  5. Lướt đủ thời lượng quy định mỗi ngày để đạt mốc xu tối đa.

---

### 3.5. Đánh Giá Sản Phẩm Đã Mua (Product Review Rewards)
- **Vị trí**: Tab **Tôi** -> **Đơn mua** -> **Đã giao**.
- **Điều kiện nhận tối đa xu**:
  - Đánh giá có tối thiểu 50 ký tự có nội dung thực tế.
  - Tải lên ít nhất 1 hình ảnh sản phẩm thực tế.
  - Tải lên ít nhất 1 video sản phẩm thực tế.
- **Cách thao tác**:
  1. Vào **Tôi** -> **Đơn Mua** -> **Đã giao**.
  2. Chọn đơn hàng vừa nhận thành công -> Bấm **"Đánh giá"**.
  3. Chấm điểm số sao -> Viết nhận xét trên 50 từ -> Chọn hình ảnh & video từ thiết bị.
  4. Chọn đánh giá chi tiết (Chất lượng sản phẩm, Dịch vụ giao hàng).
  5. Bấm **"Hoàn thành"** / **"Gửi"**. Hệ thống duyệt tự động và cộng từ `200` đến `400 Shopee Xu` cho mỗi đánh giá hợp lệ.

---

### 3.6. Mua Sắm & Sử Dụng Voucher Hoàn Xu (Coin Cashback Vouchers)
- **Vị trí**: Mục **Mã Giảm Giá / Kho Voucher**.
- **Cách thao tác**:
  1. Lưu mã **Hoàn Xu Xtra** hoặc **Mã Hoàn Xu ShopeePay** trong Kho Voucher.
  2. Khi tiến hành mua sản phẩm hoặc thanh toán đơn hàng, tại màn hình **Thanh Toán**:
  3. Nhấp chọn **Shopee Voucher** -> Áp dụng mã **Hoàn X% Xu**.
  4. Xác nhận đặt hàng và hoàn tất thanh toán.
  5. Sau khi đơn hàng hoàn thành (người dùng bấm "Đã nhận được hàng" hoặc hết thời hạn khiếu nại), số xu thưởng sẽ tự động cộng vào Ví Shopee Xu.

---

### 3.7. Thanh Toán Hóa Đơn, Nạp Thẻ Điện Thoại & Dịch Vụ
- **Vị trí**: Trang chủ -> Mục **"Nạp thẻ, Dịch vụ & Phim"**.
- **Cách thao tác**:
  1. Chọn dịch vụ cần thanh toán (Điện, Nước, Internet, Nạp ĐT, Vé xem phim).
  2. Áp mã hoàn xu áp dụng cho dịch vụ.
  3. Thực hiện thanh toán qua ShopeePay hoặc Ngân hàng liên kết.
  4. Nhận Xu hoàn tương ứng sau khi giao dịch thành công.

---

### 3.8. Săn Xu Từ Các Sự Kiện Khuyến Mãi Đại Tiệc (Campaign Events)
- Vào các ngày Siêu Sale lớn như `1/1`, `9/9`, `11/11`, `12/12` hoặc Sale Giữa Tháng (`15th`), Sale Lương Về (`25th`):
  - Tham gia **Khung Giờ Đếm Ngược Săn Xu** trên Trang chủ.
  - Tham gia các bài viết / Minigame trên trang Fanpage Facebook Shopee hoặc Shopee Feed để nhận mã redeem code xu.

---

## 4. QUY TRÌNH TỐI ƯU HÓA HÀNG NGÀY ĐỂ KIẾM TỐI ĐA SHOPEE XU (DAILY COIN ROUTINE)

Dưới đây là lịch trình thao tác gợi ý giúp thu thập xu hiệu quả nhất mỗi ngày:

| BƯỚC | TÍNH NĂNG | THỜI GIAN DỰ KIẾN | THAO TÁC CHÍNH | ƯỚC TÍNH XU |
| :---: | :--- | :---: | :--- | :---: |
| **1** | Điểm danh daily | 10 giây | Vào Săn Xu -> Bấm Điểm danh | 100 - 1,000 Xu |
| **2** | Nông trại Shopee | 1 phút | Tưới nước, thu hoạch cây xu | 100 - 500 Xu |
| **3** | Xem Shopee Video | 5 - 10 phút | Lướt video đến khi hết hạn mức ngày | 200 - 1,000 Xu |
| **4** | Xem Shopee Live | 10 - 15 phút | Chọn live có biểu tượng túi xu -> Săn lì xì | 200 - 2,000 Xu |
| **5** | Đánh giá đơn mua | 2 phút | Đánh giá có hình + video các đơn đã nhận | 200 - 400 Xu / đơn |
| **6** | Shopee Games | 5 phút | Quay Vòng quay may mắn & chơi đập kẹo | Vouchers / Xu |

---

## 5. CÁCH QUẢN LÝ VÀ KIỂM TRA SHOPEE XU

1. **Kiểm tra số dư & Hạn sử dụng**:
   - Vào tab **Tôi** -> Chọn **Shopee Xu**.
   - Màn hình hiển thị: Số xu hiện có, số xu sắp hết hạn vào cuối tháng.
2. **Xem Lịch sử giao dịch Xu**:
   - Bấm vào số dư Xu để xem chi tiết lịch sử **Cộng xu** (từ đâu) và **Trừ xu** (đã dùng vào đơn nào).
3. **Mẹo tránh mất xu hết hạn**:
   - Sử dụng xu cho các đơn hàng nhỏ hoặc dùng xu đổi voucher giảm giá trước thời hạn hết hiệu lực.
