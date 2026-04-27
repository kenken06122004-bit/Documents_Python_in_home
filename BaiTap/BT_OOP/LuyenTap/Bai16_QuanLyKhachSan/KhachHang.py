from Nguoi import nguoi
class khachHang(nguoi):
    def __init__(self, ma, ten, sdt, diaChi):
        super().__init__(ma, ten)
        self.sdt = sdt
        self.diaChi = diaChi
    def hienThi(self):
        print(f"MaKH: {self.ma:5} | TenKH: {self.ten:20} | SDT: {self.sdt:12} | DiaChi: {self.diaChi}")