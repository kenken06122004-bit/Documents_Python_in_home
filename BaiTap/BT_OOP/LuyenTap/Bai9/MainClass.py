from DanhSachNhanVien import danhSach
ds = danhSach()
while True:
    print("===== CHUC NANG =====")
    print("\n 0 = Ket thuc chuong trinh \n 1 = Nhap nhan vien \n 2 = Xuat danh sach nhan vien \n 3 = Tinh tong luong toan bo nhan vien \n 4 = Sap xep nhan vien \n 5 = Dem so nhan vien tung loai")
    try:
        menu = int(input("Nhap: "))
    except Exception as e:
        print(e)
        continue
    match menu:
        case 0:
            break
        case 1: 
            ds.themNV()
        case 2: 
            ds.xuatNV()
        case 3:
            ds.tinhTongLuong()
        case 4:
            ds.sapXepTheoLuong()
        case 5: 
            ds.demSoNhanVienTungLoai()
        case _: 
            print("Chi nhap tu 0 den 5")