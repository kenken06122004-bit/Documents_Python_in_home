from PhuongTien import PhuongTien
from KhuyenMai import KhuyenMai
class Oto(PhuongTien,KhuyenMai):
    def __init__(self, maPT="", hangSX="", gia=0, namSX=0, soCho = 0):
        super().__init__(maPT, hangSX, gia, namSX)
        self.soCho = soCho
    def tinhThue(self):
        return self.gia * 0.1
    def tinhKhuyenMai(self):
        return self.gia * 0.05
    def xuat(self):
        super().xuat()
        print(f"soCho = {self.soCho} | thue = {self.tinhThue()} | khuyenMai = {self.tinhKhuyenMai()}")