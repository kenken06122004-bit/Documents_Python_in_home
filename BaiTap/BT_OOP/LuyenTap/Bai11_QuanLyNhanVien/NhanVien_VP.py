from NhanVien import nhanVien
class nhanVien_VP(nhanVien):
    def __init__(self, maNV="", hoTen="", luongCB=0, soNgayLam = 0):
        super().__init__(maNV, hoTen, luongCB)
        self.soNgayLam = soNgayLam
    def nhap(self):
        super().nhap()
        self.soNgayLam = int(input("Nhap so ngay lam viec: "))
    def xuat(self):
        super().xuat()
        print(f"{self.soNgayLam}")
    def tinhLuong(self):
        return self.luongCB + self.soNgayLam * 100