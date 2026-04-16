from MonAn import MonAn
class trangMieng(MonAn):
    def __init__(self, maMon="", tenMon="", gia=0, giamGia=0):
        super().__init__(maMon, tenMon, gia)
        self.giamGia = giamGia
    def xuat(self):
        print(f"Giam gia: -{self.giamGia}")
    def tinhGia(self):
        return self.gia - self.giamGia