from NhanVien import nhanVien
class nhanVien_SX(nhanVien):
    def __init__(self, maNV="", hoTen="", luongCB=0, soSanPham = 0):
        super().__init__(maNV, hoTen, luongCB)
        self.soSanPham = soSanPham
    def xuat(self):
        super().xuat()
        print(f"{self.soSanPham}")
    def tinhLuong(self):
        return self.luongCB + self.soSanPham * 200