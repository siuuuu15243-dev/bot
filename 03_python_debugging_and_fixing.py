"""
03_PYTHON_DEBUGGING_AND_FIXING.PY
==================================
Chủ đề: Quy trình Tư duy & Kỹ thuật Fix Bug Chuyên Nghiệp

QUY TRÌNH 5 BƯỚC THỰC CHIẾN KHI GẶP BUG:
1. Replicate Bug (Tạo lại bug): Xác định chính xác bước/đầu vào nào gây ra lỗi.
2. Read Traceback (Đọc Traceback): Đọc từ DƯỚI LÊN TRÊN để biết Exception type và dòng code bị lỗi.
3. Isolate the Root Cause (Cô lập nguyên nhân gốc rễ): Dùng Logging/Debugger/Unit Test thay vì đoán mò.
4. Apply Fix & Refactor (Thao tác sửa lỗi): Sửa lỗi mà không làm hỏng các tính năng cũ.
5. Add Automated Tests (Viết Test phòng ngừa): Đảm bảo bug này KHÔNG BAO GIỜ quay trở lại.
"""

import logging
import unittest

# ==========================================
# 1. THAY THẾ PRINT BẰNG LOGGING CHUYÊN NGHIỆP
# ==========================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s"
)
logger = logging.getLogger(__name__)


def calculate_average_discount(prices: list[float], discount_percent: float) -> float:
    """
    Hàm tính giá bình quân sau khi giảm giá.
    
    BUG THƯỜNG GẶP TRONG CODE BỊ LỖI:
    - Danh sách `prices` rỗng -> ZeroDivisionError
    - `discount_percent` ngoài khoảng [0, 100]
    - Phần tử trong `prices` không phải kiểu số -> TypeError
    """
    logger.debug(f"Đầu vào: prices={prices}, discount_percent={discount_percent}")

    # FIX BUG 1: Kiểm tra danh sách rỗng
    if not prices:
        logger.warning("Danh sách giá rỗng, trả về giá trị mặc định 0.0")
        return 0.0

    # FIX BUG 2: Validate tham số giảm giá
    if not (0 <= discount_percent <= 100):
        raise ValueError(f"Tỷ lệ giảm giá không hợp lệ: {discount_percent}%. Phải từ 0 đến 100.")

    # FIX BUG 3: Kiểm tra kiểu dữ liệu các phần tử
    total_discounted_price = 0.0
    for price in prices:
        if not isinstance(price, (int, float)):
            raise TypeError(f"Giá trị không hợp lệ trong danh sách: {price} (Kiểu: {type(price)})")
        
        discounted = price * (1 - discount_percent / 100)
        total_discounted_price += discounted

    avg_price = total_discounted_price / len(prices)
    logger.info(f"Tính toán thành công! Giá trung bình sau giảm giá: {avg_price:.2f}")
    return avg_price


# ==========================================
# 2. VIẾT UNIT TEST ĐỂ KHÔNG BAO GIỜ BỊ REGRESSION BUG
# ==========================================

class TestCalculateAverageDiscount(unittest.TestCase):

    def test_valid_input(self):
        """Test trường hợp dữ liệu chuẩn."""
        prices = [100.0, 200.0, 300.0]
        result = calculate_average_discount(prices, 10)  # Giảm 10%
        self.assertAlmostEqual(result, 180.0)

    def test_empty_prices_list(self):
        """Test trường hợp danh sách rỗng (Phòng tránh ZeroDivisionError)."""
        result = calculate_average_discount([], 10)
        self.assertEqual(result, 0.0)

    def test_invalid_discount_percent(self):
        """Test trường hợp discount vượt quá phạm vi."""
        with self.assertRaises(ValueError):
            calculate_average_discount([100.0], 150)

    def test_invalid_data_type(self):
        """Test trường hợp dữ liệu chứa chuỗi thay vì số."""
        with self.assertRaises(TypeError):
            calculate_average_discount([100.0, "invalid_number"], 10)


if __name__ == "__main__":
    print("--- CHẠY KIỂM THỬ THỰC TẾ ---")
    
    # 1. Chạy hàm với dữ liệu đúng
    calculate_average_discount([500.0, 1000.0], 20)

    # 2. Chạy bộ Unit Tests để xác nhận toàn bộ trường hợp
    print("\n--- CHẠY UNIT TEST ---")
    unittest.main(exit=False)
