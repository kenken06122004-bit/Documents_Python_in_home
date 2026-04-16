from DanhSachNhanVien import danhSachNV
ds = danhSachNV()
while True:
    print("\n====== CHUC NANG ======")
    print("0. Ket thuc chuong trinh")
    print("1. Doc file")
    print("2. Ghi file")
    print("3. Xuat danh sach")
    print("4. Tinh tong luong nhan vien")
    menu = int(input("Nhap: "))
    match menu:
        case 0:
            print("Ket thuc chuong trinh")
            break
        case 1: 
            ds.docFile()
        case 2: 
            ds.ghiFile()
        case 3: 
            ds.xuat()
        case 4: 
            ds.tinhTongLuong()
        case _:
            print("Chi nhap tu 1 den 4")
