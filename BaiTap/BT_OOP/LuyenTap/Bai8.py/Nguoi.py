class People:
    def __init__(self):
        self.hoTen = ""
        self.tuoi = 0
        self.diaChi = ""
    def themThongTin(self):
        self.hoTen = input("Nhap ho ten: ")
        self.tuoi = int(input("Nhap so tuoi: "))
        self.diaChi = input("Nhap dia chi: ")
    def xuatThongTin(self):
        print("hoTen = {0} | tuoi = {1} | diaChi = {2} | ".format(self.hoTen,self.tuoi,self.diaChi),end="")