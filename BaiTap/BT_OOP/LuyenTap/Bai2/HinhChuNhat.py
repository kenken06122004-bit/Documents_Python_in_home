class HCN:
    def __init__(self):
        self.chieuDai = 0
        self.chieuRong = 0
    def nhapThongTin(self):
        self.chieuDai = int(input("Nhap chieu dai = "))
        self.chieuRong = int(input("Nhap chieu rong = "))
    def dienTich(self):
        return self.chieuDai * self.chieuRong
    def chuVi(self):
        return (self.chieuRong + self.chieuDai) * 2
    