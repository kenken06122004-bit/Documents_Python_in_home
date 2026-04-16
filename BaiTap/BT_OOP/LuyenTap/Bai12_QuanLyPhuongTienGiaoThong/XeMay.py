from PhuongTien import PhuongTien
from KhuyenMai import KhuyenMai
class xeMay(PhuongTien,KhuyenMai):
    def __init__(self, maPT="", hangSX="", gia=0, namSX=0, congSuat=0):
        super().__init__(maPT, hangSX, gia, namSX)
        self.congSuat = congSuat
    def tinhThue(self):
        return self.gia * 0.05
    def tinhKhuyenMai(self):
        return self.gia * 0.02
    def xuat(self):
        super().xuat()
        print(f"congSuat = {self.congSuat} | thue = {self.tinhThue()} | khuyenMai = {self.tinhKhuyenMai()}")