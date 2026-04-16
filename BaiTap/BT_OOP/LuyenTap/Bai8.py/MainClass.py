from DanhSachSinhVien import DanhSachSV
ds = DanhSachSV()
while True:
    print("\n===== MENU =====")
    print("1. Thêm sinh viên")
    print("2. Xuất danh sách sinh viên")
    print("3. Sinh viên giỏi nhất")
    print("4. Sắp xếp theo điểm trung bình")
    print("0. Thoát")
    try:
        menu = int(input("Chọn chức năng: "))
    except Exception as e:
        print(e)
        continue
    match menu:
        case m if m == 0:
            print("Ket thuc chuong trinh") 
            break
        case m if m == 1:
            ds.themSV()
        case m if m == 2: 
            ds.xuatDS()
        case m if m == 3: 
            ds.timSV_gioiNhat()
        case m if m == 4: 
            ds.sapXepTheoDiemTB()
        case _: 
            print("Chi nhap tu 0 den 4")