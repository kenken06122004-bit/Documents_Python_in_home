from Sach import Sach
class SachTK(Sach):
    def __init__(self, maSach="", tenSach="", tacGia="", gia=0, thue = 0.0):
        super().__init__(maSach, tenSach, tacGia, gia)
        self.thue = thue
    def tinhGiaSauThue(self):
        return self.gia + self.thue
    def hienThi(self):
        super().hienThi()
        print(f"thue = {self.thue}")