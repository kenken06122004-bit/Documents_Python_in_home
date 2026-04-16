from NhanVien import NV
class HanhChinh(NV):
    def __init__(self):
        super().__init__()
        self.heSoLuong = 0
    def nhap(self):
        super().nhap()
        self.heSoLuong = int(input("Nhap he so luong"))
    def xuat(self):
        super().xuat()
        print("heSoLuong = {0}".format(self.heSoLuong))
    def tinhLuong(self):
        return self.luongCB * self.heSoLuong    
    