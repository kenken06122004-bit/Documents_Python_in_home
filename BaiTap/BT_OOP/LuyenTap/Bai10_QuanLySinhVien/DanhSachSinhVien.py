from SinhVien import sv
class danhSach:
    def __init__(self):
        self.dsSinhVien: list[sv] = []
    def nhapSinhVien(self):
        sinhVien = sv()
        sinhVien.nhap()
        self.dsSinhVien.append(sinhVien)
        print("Danh sach sinh vien sau khi nhap la: ")
        self.xuatSinhVien()
    def xuatSinhVien(self):
        if not self.dsSinhVien:
            print("Danh sach rong")
            return
        print("====== DANH SACH SINH VIEN ======")
        for x in self.dsSinhVien:
            x.xuat()
    def docFile(self):
        try:
            with open("docFile.txt","r",encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line == "":
                        continue
                    arr = line.split(",")
                    maSV = arr[0]
                    ten = arr[1]
                    tuoi = int(arr[2])
                    gioiTinh = arr[3]
                    diemToan = float(arr[4])
                    diemLy = float(arr[5])
                    diemHoa = float(arr[6])
                    NewSinhVien = sv(maSV,ten,tuoi,gioiTinh,diemToan,diemLy,diemHoa)
                    self.dsSinhVien.append(NewSinhVien)
            print("Doc file thanh cong")
        except Exception as e:
            print("Loi doc file: ",e)
    def ghiFile(self):
        if not self.dsSinhVien:
            print("Danh sach rong")
            return
        try:
            with open("D:\\Python_in_VScode\\Data_for_luyenTap\\ghiFile_15022026.txt","w",encoding="utf-8") as f:
                for x in self.dsSinhVien:
                    f.write(f"{x.maSV}, {x.ten}, {x.tuoi}, {x.gioiTinh}, {x.diemToan}, {x.diemLy}, {x.diemHoa}\n")
            print("Ghi file thanh cong")
        except Exception as e:
            print("Loi ghi file: ",e)
    def xoaSinhVien(self):
        if not self.dsSinhVien:
            print("Danh sach rong")
            return
        canXoa = input("Nhap ma sinh vien can xoa: ")
        timThay = False
        for x in self.dsSinhVien:
            if x.maSV == canXoa:
                self.dsSinhVien.remove(x)
                timThay = True
                break
        if timThay == True:
            print("Xoa thanh cong")
        else:
            print("Khong ton tai de xoa")
    def tinhtongDiemTB(self):
        if not self.dsSinhVien:
            print("Danh sach rong")
            return
        tongTB = 0.0
        demSV = 0
        for x in self.dsSinhVien:
            tongTB += x.tinhdiemTB()
            demSV += 1
        print(f"Tong diem TB cua toan bo sinh vien la: {tongTB/demSV}")