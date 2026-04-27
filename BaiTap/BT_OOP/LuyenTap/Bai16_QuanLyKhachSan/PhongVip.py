from Room import Phong
class phongVip(Phong):
    def tinhTien(self, soNgay):
        tong = self.gia * soNgay
        if soNgay >= 5:
            tong = tong * 0.9
        return tong