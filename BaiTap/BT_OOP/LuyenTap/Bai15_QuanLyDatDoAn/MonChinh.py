from MonAn import MonAn
class monChinh(MonAn):
    def __init__(self, maMon="", tenMon="", gia=0, size=""):
        super().__init__(maMon, tenMon, gia)
        self.size = size
    def xuat(self):
        super().xuat()
        print(f"Size: {self.size}")
    def tinhGia(self):
        if self.size.startswith("S"):
            return self.gia
        elif self.size.startswith("M"):
            return self.gia * 2
        elif self.size.startswith("L"):
            return self.gia * 3
        else:
            return 0
