from MonAn import MonAn
class doUong(MonAn):
    def __init__(self, maMon="", tenMon="", gia=0, coDa = True):
        super().__init__(maMon, tenMon, gia)
        self.coDa = coDa
    def xuat(self):
        super().xuat()
        print(f"Ice: {'Co' if self.coDa == True else 'Khong'}")
    def tinhGia(self):
        if self.coDa == True:
            return self.gia + 5000
        else:
            return self.gia