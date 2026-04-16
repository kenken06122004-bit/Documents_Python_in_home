from Nguoi import People
class SV(People):
    def __init__(self):
        super().__init__()
        self.maSV = ""
        self.diemToan = 0
        self.diemLy = 0
        self.diemHoa = 0
    def themThongTin(self):
        super().themThongTin()
        self.maSV = int(input("Nhap ma sinh vien: "))
        self.diemToan = int(input("Nhap diem toan: "))
        self.diemLy = int(input("Nhap diem ly: "))
        self.diemHoa = int(input("Nhap diem hoa: "))
    def tinhDiemTB(sefl):
        return ( sefl.diemToan + sefl.diemLy + sefl.diemHoa) / 3
    def xepLoai(sefl):
        diemTB = sefl.tinhDiemTB()
        if diemTB >= 8:
            return "Gioi"
        elif diemTB >= 6.5 and diemTB <= 7.9:
            return "Kha"
        elif diemTB >= 5 and diemTB <= 6.4:
            return "Trung binh"
        else:
            return "Yeu"
    def xuatThongTin(self):
        super().xuatThongTin() 
        print("maSV = {0} | diemToan = {1} | diemLy = {2} | diemHoa = {3} | diemTB = {4} | xepLoai = {5}".format(self.maSV,self.diemToan,self.diemLy,self.diemHoa,self.tinhDiemTB(),self.xepLoai()), end="\n")