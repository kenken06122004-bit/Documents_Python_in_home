"""Viết chương trình tra cứu số điện thoại:

Có sẵn dictionary:

so_dien_thoai = {"Hùng": "0901", "An": "0902", "Bình": "0903"}

Người dùng nhập tên → in ra số điện thoại tương ứng.

Nếu không có → in "Không tìm thấy tên này"."""
so_dien_thoai = {"Hùng": "0901", "An": "0902", "Bình": "0903"}
ten = input("Nhập tên người dùng cần lấy số điện thoại: ")
if ten in so_dien_thoai:
    print("Số điện thoại của người dùng tên ",ten," là: ",so_dien_thoai[ten])
else: 
    print("Không tìm thấy")