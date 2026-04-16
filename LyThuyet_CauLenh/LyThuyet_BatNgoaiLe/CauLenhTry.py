"""
Câu lệnh try_except dùng để bắt ngoại lệ của dữ liệu input vào chương trình
Cú pháp như sau:
    try:
        # Đoạn code dự đoán có lỗi 
    except:
        # Hành động khi lỗi xảy ra
    else:
        # Thực thi đoạn này nếu như không có lỗi
    finally:
        # Cho phép bạn thực thi, mà bât kể kết quả của các khối try có bị lỗi hay không
"""
# Ví dụ: 
try:
    a = int(input("Nhap vao so nguyen a: "))
    print(a)
except Exception as e:
    print("Nhap du lieu khong chinh xac")
    print(e)
else:
    print("Khong co loi xay ra")
finally:
    print("Ket thuc chuong trinh")