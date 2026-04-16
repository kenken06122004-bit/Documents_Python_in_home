class people:
    def __init__(self,ten="",tuoi=0,gioiTinh=""):
        self.ten = ten
        self.tuoi = tuoi
        self.gioiTinh = gioiTinh
    def xuat(self):
        print(f"ten = {self.ten} | tuoi = {self.tuoi} | gioiTinh = {self.gioiTinh} | ",end="")
    def nhap(self):
        self.ten = input("Nhap ten: ")
        self.tuoi = input("Nhap so tuoi: ")
        self.gioiTinh = input("Nhap gioi tinh: ")
