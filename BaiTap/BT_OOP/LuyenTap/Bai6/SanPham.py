class SP:
    def __init__(self):
        self.tenSP = "none"
        self.giaBan = 0
        self.soLuong = 0
    def thanhTien(self):
        return self.giaBan * self.soLuong
    def nhap(self):
        self.tenSP = input("Nhap ten san pham: ")
        self.giaBan = int(input("Nhap gia ban: "))
        self.soLuong = int(input("Nhap so luong: "))
    def xuat(self):
        print("TenSP: {0} | Giaban: {1} | SL: {2} | ThanhTien: {3}".format(self.tenSP,self.giaBan,self.soLuong,self.thanhTien()))
