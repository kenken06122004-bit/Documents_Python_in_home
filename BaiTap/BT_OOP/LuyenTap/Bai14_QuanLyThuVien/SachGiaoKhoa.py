from Sach import Sach
class SachGK(Sach):
    def __init__(self, maSach="", tenSach="", tacGia="", gia=0, tinhTrang = True):
        super().__init__(maSach, tenSach, tacGia, gia)
        self.tinhTrang = tinhTrang
    def tinhGiaSauThue(self):
        if self.tinhTrang == True:
            return self.gia
        else:
            return self.gia * 0.5
    def hienThi(self):
        super().hienThi()
        print(f"tinhTrang = {'Moi' if self.tinhTrang == True else 'Cu'}")