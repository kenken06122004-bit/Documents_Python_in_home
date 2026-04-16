from Nguoi import people
class SV(people):
    def __init__(self):
        super().__init__()
        self.diemTB = 0.0
    def nhap(self):
        super().nhap()
        self.diemTB = float(input("Nhap diem trung binh: "))
    def xepLoai(self):
        if self.diemTB >= 8:
            return "Gioi"
        elif self.diemTB >= 6.5:
            return "Kha"
        elif self.diemTB >= 5:
            return "Trung binh"
        else: 
            return "Yeu"
    def xuat(self):
        super().xuat() # Gọi phương thức ở lớp cha
        print("Diem trung: {0} | XepLoai: {1}".format(self.diemTB,self.xepLoai()))