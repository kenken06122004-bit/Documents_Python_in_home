import psycopg2
"""Đây là thư viện chuyên dùng để Python kết nối với PostgreSQL
Có thể dùng để: 
1) Mở kết nối DB
2) Tạo cursor
3) Chạy SQL
4) fetch data
5) Commit transaction"""
import pandas as pd
from sqlalchemy import create_engine
"""Dùng để import function create_engine() của SQLAlchemy, SQLAlchemy là cầu nối giúp 
pandas giao tiếp với DB"""
from sqlalchemy.engine import URL
"""Dùng để tạo chuỗi kết nối DB an toàn, tránh lỗi password khi có ký tự đặc biệt"""
def fetch_data():
    """1) Tạo biến ban đầu rỗng:"""
    connection = None
    cursor = None
    """Để tránh lỗi nếu kết nối thất bại vì vẫn cần close"""
    try:
        """Mở kết nối đến PostgreSQL server"""
        connection = psycopg2.connect(
            user = "postgres",
            password = "Nguyenvanphi2004@",
            host = "localhost", # Máy chủ DB nằm trên máy hiện tại
            port = "5432", # Port mặc định của PostgreSQL
            database = "SQL_learn_in_home" # Tên của DB cần truy cập
        )
        # Tạo đối tượng cursor để thực thi lệnh SQL:
        cursor = connection.cursor() # cursor giống như tay điểu khiển
        # Thực thi câu lệnh truy vấn dữ liệu từ bảng actor:
        # Lấy 10 dòng đầu tiên để kiểm tra:
        print("Dang truy van du lieu tu bang 'actor'...")
        cursor.execute("SELECT actor_id, first_name, last_name, last_update FROM actor LIMIT 10")
        # Lấy toàn bộ kết quả trả về:
        records = cursor.fetchall() # Kết quả là list tuple
        print(f"So luong dong lay duoc: {len(records)}")
        print("-" * 50)
        # Duyệt qua từng dòng dữ liệu và sử dụng:
        for row in records:
            id_dien_vien = row[0]
            ho_ten = f"{row[1]} {row[2]}"
            cap_nhat = row[3]
            print(f"ID: {id_dien_vien} | Ten: {ho_ten} | Cap nhat lan cuoi: {cap_nhat}")
    except (Exception, psycopg2.Error) as error:
        print(f"Loi khi ket noi: {error}")
    finally:
        if connection:
            if 'connection' in locals() and connection:
                if 'cursor' in locals() and cursor: 
                    cursor.close()
                connection.close()
                print("Da dong ket noi PostgresSQL")

# Dùng pandas:
def fetch_data_with_pandas():
    try:
        # 1) Khởi tạo thông tin kết nối:
        """Tạo connection string chuẩn. Tự xử lý password đặc biệt"""
        url = URL.create(
            drivername="postgresql+psycopg2",
            username="postgres",
            password="Nguyenvanphi2004@",
            host="127.0.0.1",
            port=5432,
            database="SQL_learn_in_home"
        )
        
        # 2) Tạo Engine kết nối (định dạng chuẩn của SQLAlchemy)
        engine = create_engine(url) # engine = trung tâm giao tiếp DB

        # 3) Sử dụng pandas để đọc dữ liệu từ SQL trực tiếp vào DataFrame:
        print("Dang doc du lieu bang Pandas...")
        query = "SELECT * FROM actor LIMIT 10" # Lưu SQL vào biến
        df = pd.read_sql(query, engine) # Thực hiện SQL và đưa kết quả vào DataFrame

        # 4) Sử dụng dữ liệu trong DataFrame:
        print(df)
    except Exception as e:
        print(f"Loi khi xu ly voi Pandas: {e}")
    finally:
        # SQLAlchemy tự động quản lý kết nối, không cần phải đóng thủ công như psycopg2
        print("-" * 30)
        print("Hoan tat xu ly du lieu.")

if __name__ == "__main__": # Chỉ chạy khi file này được chạy trực tiếp
    #fetch_data()
    fetch_data_with_pandas()