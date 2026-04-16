"""Xây dựng chương trình rút thăm trúng thưởng với các chức năng sau:
1) Thêm một số điện thoại dự thưởng vào thùng
2) Xóa một số điện thoại dự thưởng ra khỏi thùng
3) Quay số ngẫu nhiên lấy ra một số điện thoại trúng thưởng"""

# Ngoài lề xíu: Một vài tình huống mà chúng ta dùng Set để lưu trữ
"""Ví dụ:   - Mã căn cước công dân
            - Biển số xe
            - Số điện thoại
            - v.v"""
import random
# Khai báo Set:
thungPhieu = set()
while(True):
    menu = int(input("Nhập: 0 = thoát | 1 = Thêm | 2 = Xóa | 3 = Quay số \n"))
    match menu:
        case 0: break
        case 1: 
            soDienThoai_DT = input("Nhập vào số điện thoại dự thưởng: ")
            thungPhieu.add(soDienThoai_DT)
        case 2:
            soDienThoai_DT_canXoa = input("Nhập vào số điện thoại cần xóa: ")
            thungPhieu.discard(soDienThoai_DT_canXoa)
        case 3:
            if len(thungPhieu) == 0:
                print("Thùng phiếu trống, không thể quay số!")
            else:
                soTrungThuong = random.choice(list(thungPhieu))
                print("Số điện thoại trúng thưởng là: ",soTrungThuong)
        case _: print("Chỉ nhập từ 0 đến 3")