from QuanLyKhachSan import QuanLyKhachSan
ql = QuanLyKhachSan()
ql.docFile()
while True:
    print("\n============= CHUC NANG =============")
    print("0. Ket thuc chuong trinh")
    print("1. Xem danh sach cac muc theo dang binh thuong")
    print("2. Xem danh sach cac muc theo dang pandas")
    print("3. Dat phong")
    print("4. Tra phong")
    try:
        op = int(input("Nhap lua chon: "))
    except Exception as e:
        print("Loi: ",e)
    else:
        if op == 0:
            print("Tam biet")
            break
        elif op == 1:
            ql.hienThi()
        elif op == 2:
            ql.hienThi_pandas()
        elif op == 3:
            ql.bookPhong()
        elif op == 4:
            ql.checkOutRoom()
        else:
            print("Chi nhap tu 0 --> 4")