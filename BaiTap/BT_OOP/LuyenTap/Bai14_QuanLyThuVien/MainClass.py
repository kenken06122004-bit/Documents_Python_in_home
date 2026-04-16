from DanhSachSach import DanhSachSach
ds = DanhSachSach()
while(True):
    print("============== MENU ==============")
    print("1. Doc file cach thong thuong")
    print("2. Ghi file cach thong thuong")
    print("3. Xuat cach thong thuong")
    print("4. Doc file cach pandas")
    print("5. Ghi file cach pandas")
    print("6. Xuat cach pandas")
    try:
        op = int(input("Nhap lua chon: "))
    except Exception as e:
        print("Chi duoc nhap so")
    match(op): 
        case 0:
            print("Ket thuc chuong trinh")
            break
        case 1: 
            ds.docFile("docFile.txt")
        case 2: 
            ds.ghiFile("ghiFile.txt")
        case 3:
            ds.xuatForDocFileThuong()
        case _:
            print("Chi duoc nhap trong khoang cho phep cua menu")