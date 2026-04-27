from Nguoi import nguoi
class nhanVien(nguoi):
    def __init__(self, ma, ten, chucVu, luong):
        super().__init__(ma, ten)
        self.chucVu = chucVu
        self.luong = luong
    def hienThi(self):
        print(f"MaNV: {self.ma:5} | TenNV: {self.ten:20} | ChucVu: {self.chucVu:12} | Luong: {self.luong}")