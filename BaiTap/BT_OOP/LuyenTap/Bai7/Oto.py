from PhuongTien import Xe
class Oto(Xe):
    def __init__(self):
        super().__init__()
        self.soChoNgoi = 0
    def nhap(self):
        super().nhap()
        self.soChoNgoi = int(input("Nhap so cho ngoi: "))
    def xuat(self):
        super().xuat()
        print("| So cho ngoi: {0}".format(self.soChoNgoi))