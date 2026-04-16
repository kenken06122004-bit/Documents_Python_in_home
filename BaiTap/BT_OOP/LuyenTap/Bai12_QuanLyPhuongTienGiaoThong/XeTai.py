from PhuongTien import PhuongTien
from KhuyenMai import KhuyenMai
class xeTai(PhuongTien,KhuyenMai):
    def __init__(self, maPT="", hangSX="", gia=0, namSX=0, taiTrong=0):
        super().__init__(maPT, hangSX, gia, namSX)
        self.taiTrong = taiTrong
    def tinhThue(self):
        return self.gia * 0.15
    def tinhKhuyenMai(self):
        return self.gia * 0.07
    def xuat(self):
        super().xuat()
        print(f"taiTrong = {self.taiTrong} | thue = {self.tinhThue()} | khuyenMai = {self.tinhKhuyenMai()}")