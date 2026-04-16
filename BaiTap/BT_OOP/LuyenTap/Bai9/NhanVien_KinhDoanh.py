from NhanVien import NV
class KinhDoanh(NV):
    def __init__(self):
        super().__init__()
        self.doanhSo = 0
        self.hoaHong = 0.05 # Hoa hong 5%
    def nhap(self):
        super().nhap()
        self.doanhSo = int(input("Nhap doanh so"))
    def xuat(self):
        super().xuat()
        print("doanhSo = {0}".format(self.doanhSo))
    def tinhLuong(self):
        return self.luongCB + self.doanhSo * self.hoaHong    