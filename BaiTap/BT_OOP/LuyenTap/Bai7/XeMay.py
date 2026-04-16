from PhuongTien import Xe
class xeMay(Xe):
    def __init__(self):
        super().__init__()
        self.congSuat = 0
    def nhap(self):
        super().nhap()
        self.congSuat = int(input("Nhap cong suat: "))
    def xuat(self):
        super().xuat()
        print("| Cong suat: {0}".format(self.congSuat))