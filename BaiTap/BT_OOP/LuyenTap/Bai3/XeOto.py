class Oto:
    def __init__(self):
        self.hangXe = "Chua co"
        self.mauSac = "Chua co"
        self.giaBan = 0.0
    def nhap(self):
        self.hangXe = input("Nhap hang xe: ")
        self.mauSac = input("Nhap mau sac xe: ")
        self.giaBan = float(input("Nhap gia ban: "))
    def xuat(self):
        print("Hang xe: {0} | Mau sac: {1} | Gia ban: {2}".format(self.hangXe,self.mauSac,self.giaBan))
    