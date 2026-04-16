from Nguoi import people
class sv(people):
    def __init__(self,maSV="",ten="",tuoi=0,gioiTinh="",diemToan=0.0,diemLy=0.0,diemHoa=0.0):
        super().__init__(ten,tuoi,gioiTinh)
        self.maSV = maSV
        self.diemToan = diemToan
        self.diemLy = diemLy
        self.diemHoa = diemHoa
    def xuat(self):
        print(f"maSV = {self.maSV} | ",end="")
        super().xuat()
        print(f"diemToan = {self.diemToan} | diemLy = {self.diemLy} | diemHoa = {self.diemHoa} | diemTB = {self.tinhdiemTB()}")
    def nhap(self):
        self.maSV = input("Nhap ma sinh vien: ")
        super().nhap()
        self.diemToan = float(input("Nhap so diem Toan: "))
        self.diemLy = float(input("Nhap so diem Ly: "))
        self.diemHoa = float(input("Nhap so diem Hoa: "))
    def tinhdiemTB(self):
        return (self.diemToan * 2 + self.diemLy + self.diemHoa) / 4 