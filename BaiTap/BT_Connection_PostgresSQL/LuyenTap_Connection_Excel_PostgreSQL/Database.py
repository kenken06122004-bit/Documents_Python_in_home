import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# Lệnh này cực kỳ quan trọng: Nó giúp python "Mở cửa" file .env ra
load_dotenv("Sercurity.env") 

# Kiểm tra xem file có đuôi .env cố tồn tại hay không
#if os.path.exists("Sercurity.env"):
#    print("Co file")
#else:
#    print("Khong tim thay")

# Connection details: Dùng thư viện os để lấy dữ liệu mà chúng ta đã giấu vào các biến
"""host = os.getenv('DB_host')
port = "5432"
database = os.getenv("DB_database")
username = os.getenv('DB_username')
password = os.getenv('DB_password')

# Kiểm tra xem đã đúng hay chưa: LỨU Ý: khi làm project thật thì phải xóa cái này
#print(f"Tai khoan: {username} | Mat khau: {password}")
#print(f"Database: {database}")

# Sử dụng thư viên pandas để đọc file excel:
try:
    customer = pd.read_excel("C:\\Users\\ADMIN\\Downloads\\Bảng tính không có tiêu đề.xlsx", sheet_name='Customer')
    print(customer)
except Exception as e:
    print("Loi: ", e)

# Sử dụng pandas để đưa dữ liệu vào Postgresql:
db_url = URL.create(
    drivername="postgresql+psycopg2",
    username=username,
    password=password,
    host=host,
    port=5432,
    database=database
) 
engine = create_engine(db_url)"""
class db:
    def __init__(self):
        db_url = URL.create(
            drivername="postgresql+psycopg2",
            username=os.getenv("DB_username"),
            password=os.getenv("DB_password"),
            host=os.getenv("localhost"),
            port=5432,
            database=os.getenv("DB_database")
        )
        self.engine = create_engine(db_url)
    def get_engine(self):
        return self.engine
