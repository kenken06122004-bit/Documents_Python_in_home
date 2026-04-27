from Room import Phong
class phongGiaDinh(Phong):
    def tinhTien(self, soNgay):
        tong = self.gia * soNgay
        if soNgay >= 7:
            tong = tong * 0.85
        return tong