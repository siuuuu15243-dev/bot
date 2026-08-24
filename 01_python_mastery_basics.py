"""
01_PYTHON_MASTERY_BASICS.PY
===========================
Chủ đề: Kiểu cách viết Code Python chuẩn (Pythonic Style & Clean Code)

Quy tắc cốt lõi:
1. Đọc dễ hơn viết (Readability counts).
2. Explicit tốt hơn Implicit (Rõ ràng tốt hơn mập mờ).
3. Luôn sử dụng Type Hints để giúp IDE phát hiện bug sớm.
4. Xử lý ngoại lệ cụ thể, không che giấu lỗi.
"""

from typing import List, Dict, Optional
import json


# ==========================================
# 1. TƯ DUY ĐẶT TÊN VÀ ĐỊNH DẠNG (PEP 8)
# ==========================================

# BAD CODE (Khó đọc, mập mờ)
def p(d):
    res = []
    for x in d:
        if x['a'] > 18:
            res.append(x['n'].upper())
    return res


# GOOD CODE (Pythonic, Type Hints, Rõ nghĩa)
def filter_adult_user_names(users: List[Dict[str, any]]) -> List[str]:
    """
    Lọc danh sách tên người dùng có tuổi trên 18 và viết hoa.
    """
    return [user["name"].upper() for user in users if user.get("age", 0) > 18]


# ==========================================
# 2. XỬ LÝ NGOẠI LỆ (ERROR HANDLING)
# ==========================================

# BAD CODE: Che giấu lỗi, gây khó khăn cho việc debug
def read_config_bad(file_path: str):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except:
        # Nuốt chửng mọi lỗi (KeyError, FileNotFoundError, JSONDecodeError) -> RẤT NGUY HIỂM!
        return None


# GOOD CODE: Bắt lỗi cụ thể và phản hồi rõ ràng
def read_config_good(file_path: str) -> Optional[dict]:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[ERROR] File cấu hình không tồn tại: {file_path}")
    except json.JSONDecodeError as err:
        print(f"[ERROR] File cấu hình sai định dạng JSON: {err}")
    except Exception as err:
        print(f"[ERROR] Lỗi không xác định khi đọc file: {err}")
    
    return None


# ==========================================
# 3. QUẢN LÝ TÀI NGUYÊN (CONTEXT MANAGERS)
# ==========================================

class DatabaseConnection:
    """Ví dụ về Custom Context Manager đảm bảo đóng tài nguyên ngay cả khi có lỗi."""
    def __init__(self, db_name: str):
        self.db_name = db_name

    def __enter__(self):
        print(f"-> Đang kết nối tới CSDL: {self.db_name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"<- Đã đóng kết nối CSDL: {self.db_name}")
        if exc_type:
            print(f"[WARN] Đã xảy ra ngoại lệ trong transaction: {exc_val}")
        # Tra ve False de exception tiep tuc duoc throw neu co
        return False


if __name__ == "__main__":
    # Test Clean Function
    sample_users = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 15},
        {"name": "Charlie", "age": 30}
    ]
    print("Danh sách người trưởng thành:", filter_adult_user_names(sample_users))

    # Test Resource Management
    with DatabaseConnection("production_db") as db:
        print("  [Executing SQL Queries...]")
