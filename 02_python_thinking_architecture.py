"""
02_PYTHON_THINKING_ARCHITECTURE.PY
==================================
Chủ đề: Tư duy Lập trình & Kiến trúc Phần mềm (Software Architecture & Design Patterns)

TƯ DUY LẬP TRÌNH CHUYÊN NGHIỆP:
1. Don't Repeat Yourself (DRY): Tránh lặp lại code.
2. Single Responsibility Principle (SRP): Mỗi class/hàm chỉ làm 1 việc duy nhất.
3. Loose Coupling: Giảm sự phụ thuộc cứng giữa các thành phần.
4. Refactoring: Liên tục cải tiến code cũ để sạch sẽ và tối ưu hơn.
"""

from abc import ABC, abstractmethod


# ==========================================
# 1. TƯ DUY THIẾT KẾ: TRƯỚC KHI REFACTOR (BAD ARCHITECTURE)
# ==========================================
# Lớp PaymentProcessor này ôm x ôm xụm tất cả các hình thức thanh toán.
# Khi muốn thêm cổng thanh toán mới (Momo, ZaloPay), ta BẮT BUỘC phải sửa class này (Vi phạm Open-Closed Principle).

class PaymentProcessorBad:
    def process(self, payment_type: str, amount: float):
        if payment_type == "paypal":
            print(f"Xử lý {amount}$ qua PayPal API...")
        elif payment_type == "stripe":
            print(f"Xử lý {amount}$ qua Stripe SDK...")
        elif payment_type == "crypto":
            print(f"Xử lý {amount}$ qua Web3 Provider...")
        else:
            raise ValueError("Cổng thanh toán không hỗ trợ!")


# ==========================================
# 2. TƯ DUY THIẾT KẾ: SAU KHI REFACTOR (STRATEGY PATTERN)
# ==========================================
# Áp dụng Strategy Pattern + Dependency Inversion:
# Code mới có thể mở rộng dễ dàng bằng cách thêm Class mới mà KHÔNG CẦN sửa code cũ!

class PaymentStrategy(ABC):
    """Interface định nghĩa chuẩn cho các cổng thanh toán."""
    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass


class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float) -> bool:
        print(f"[PayPal] Đã thanh toán thành công ${amount}")
        return True


class StripePayment(PaymentStrategy):
    def pay(self, amount: float) -> bool:
        print(f"[Stripe] Đã thanh toán thành công ${amount}")
        return True


class CryptoPayment(PaymentStrategy):
    def pay(self, amount: float) -> bool:
        print(f"[Crypto] Đã chuyển thành công ${amount} USDT")
        return True


class PaymentService:
    """Lớp quản lý thanh toán, không quan tâm chi tiết triển khai cụ thể."""
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def execute_payment(self, amount: float):
        if amount <= 0:
            raise ValueError("Số tiền thanh toán phải lớn hơn 0!")
        return self.strategy.pay(amount)


# ==========================================
# 3. TƯ DUY FACTORY PATTERN (KHỞI TẠO ĐỐI TƯỢNG TỰ ĐỘNG)
# ==========================================

class PaymentFactory:
    _strategies = {
        "paypal": PayPalPayment,
        "stripe": StripePayment,
        "crypto": CryptoPayment,
    }

    @classmethod
    def get_payment_method(cls, method_name: str) -> PaymentStrategy:
        strategy_cls = cls._strategies.get(method_name.lower())
        if not strategy_cls:
            raise ValueError(f"Không tìm thấy phương thức thanh toán: {method_name}")
        return strategy_cls()


if __name__ == "__main__":
    print("--- DEMO STRATEGY PATTERN ---")
    
    # Người dùng chọn phương thức thanh toán
    user_choice = "crypto"
    amount_to_pay = 150.0

    # Lấy Strategy tương ứng thông qua Factory
    payment_method = PaymentFactory.get_payment_method(user_choice)
    
    # Thực thi thanh toán
    service = PaymentService(strategy=payment_method)
    service.execute_payment(amount_to_pay)
