from DanhSachSinhVien import danhSach
ds = danhSach()
while(True):
    print("\n====== CHUC NANG ======")
    print("1. Doc file")
    print("2. Ghi file")
    print("3. Xuat danh sach")
    print("4. Them sinh vien")
    print("5. Xoa sinh vien")
    print("6. Tinh tong diemTB cua toan bo sinh vien")
    print("7. Ket thuc chuong trinh")
    try: 
        menu = int(input("Nhap: "))
    except Exception as e:
        print("Loi: ",e)
        continue
    match menu:
        case 1:
            ds.docFile()
        case 2: 
            ds.ghiFile()
        case 3: 
            ds.xuatSinhVien()
        case 4: 
            ds.nhapSinhVien()
        case 5: 
            ds.xoaSinhVien()
        case 6:
            ds.tinhtongDiemTB()
        case 7: 
            print("Ket thuc chuong trinh")
            break
        case _:
            print("Chi nhap tu 1 den 7")