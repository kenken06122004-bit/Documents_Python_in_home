# Làm việc với File trong python
# 1) Mở file trong python:

# Cú pháp: open(tên_file, chế_độ, encoding)

# Tên file:
""" Nếu file cùng cấp với file bạn chạy (Run) thì chỉ cần ghi tên file là được
Nếu khác hoặc file cần đọc, ghi,... nằm trong thư mục khác thì cần truyền đường dẫn vào tên file
"""
# Chế độ:
"""Các chế độ: 
    - r: mở file để đọc - Mặc định
    - w: mở file để ghi - Xóa nội dung cũ nếu có
    - a: ghi nối thêm (append) vào cuối file
    - r+: Vừa đọc vừa ghi
    - w+: Ghi rồi đọc lại (xóa nội dung cũ)
    - a+: Đọc và thêm (append) vào cuối file
"""
# encoding: hay còn gọi là mã hóa. Có nghĩa là cách máy tính lưu chữ cái, ký tự, dấu tiếng Việt, ký hiệu,... dưới dạng số
# mặc định chúng ta luôn ghi encoding = "utf-8" -- > phổ biến nhất và hỗ trợ hầu hết các ngôn ngữ trên TG và cả emoji
# vì nếu chúng ta đọc file có dấu tiếng việt mà không ghi encoding thì Python có thể báo lỗi
# nếu không ghi encoding, Python sẽ mặc định dùng cp1252 hoặc ANSI

# 2) Đọc file (r):
"""with open("D:\\Python_in_VScode\\LyThuyet_CauLenh\\LyThuyet_XuLy_File\\Data_for_docFile\\fileTest.txt","r",encoding="utf-8") as f:
    noiDung = f.read()
    print("Noi dung file:")
    print(noiDung)"""

# 3) Đọc từng dòng file (r):
"""with open("D:\\Python_in_VScode\\LyThuyet_CauLenh\\LyThuyet_XuLy_File\\Data_for_docFile\\fileTest.txt","r",encoding="utf-8") as f:
    print("Tung dong trong file")
    for dong in f:
        print(dong.strip())"""

# 4) Ghi file mới (w):
"""with open("D:\\Python_in_VScode\\LyThuyet_CauLenh\\LyThuyet_XuLy_File\\Data_for_docFile\\fileTest_ghi.txt","w",encoding="utf-8") as f:
    f.write("Dong 1: Xin chao \n")
    f.write("Dong 2: Toi dang hoc Python\n")
print("Da ghi file moi thanh cong")"""

# 5) Ghi nối thêm (a):
try:
    with open("D:\\Python_in_VScode\\LyThuyet_CauLenh\\LyThuyet_XuLy_File\\Data_for_docFile\\fileTest_ghi.txt","a",encoding="utf-8") as f:
        f.write("Dong 3: Them noi dung moi\n")
except Exception as e:
    print(e)
finally:
    print("Da ghi noi them noi dung moi")