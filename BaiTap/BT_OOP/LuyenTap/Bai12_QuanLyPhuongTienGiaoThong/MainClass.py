from DanhSachPhuongTien import DanhSachPT
ds = DanhSachPT()
while True:
    print("\n====== CHUC NANG ======")
    print("0. Ket thuc chuong trinh")
    print("1. Doc file")
    print("2. Ghi file")
    print("3. Xuat danh sach")
    menu = int(input("Nhap: "))
    match menu:
        case 0: 
            print("Ket thuc chuong trinh")
            break
        case 1: 
            ds.docFile()
        case 2: 
            pass
        case 3: 
            ds.xuat()
        case _:
            print("Chi nhap tu 1 den 3")