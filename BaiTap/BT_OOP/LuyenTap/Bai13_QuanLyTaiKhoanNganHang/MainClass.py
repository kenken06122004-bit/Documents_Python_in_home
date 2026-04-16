from DanhSachTaiKhoan import danhSachTK
ds = danhSachTK()
while(True):
    print("========= CHUC NANG =========")
    print("0. Ket thuc chuong trinh")
    print("1. Doc file")
    print("2. Doc file bang pandas")
    print("3. Ghi file")
    print("4. Ghi file bang pandas")
    print("5. Hien thi danh sach")
    op = int(input("Nhap lua chon: "))
    match op:
        case 0: 
            print("Ket thuc chuong trinh")
            break
        case 1: 
            ds.docFile("D:\\Python_in_VScode\\BaiTap\\BT_OOP\\LuyenTap\\Bai13_QuanLyTaiKhoanNganHang\\docFile.txt")
        case 2: 
            ds.docFile_bang_Pandas("D:\\Python_in_VScode\\BaiTap\\BT_OOP\\LuyenTap\\Bai13_QuanLyTaiKhoanNganHang\\docFile.txt")
        case 3: 
            ds.ghiFile("D:\\Python_in_VScode\\BaiTap\\BT_OOP\\LuyenTap\\Bai13_QuanLyTaiKhoanNganHang\\ghiFile1.txt")
        case 4: 
            ds.ghiFile_bang_Pandas("D:\\Python_in_VScode\\BaiTap\\BT_OOP\\LuyenTap\\Bai13_QuanLyTaiKhoanNganHang\\ghiFile2.txt")
        case 5:
            ds.xuat()
        case _:
            print("Chi nhap tu 0 den 4")