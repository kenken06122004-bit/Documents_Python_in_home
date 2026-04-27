from IThanhToan import I_ThanhToan
class Phong(I_ThanhToan):
    def __init__(self, ma, loai, gia, trangThai):
        self.ma = ma
        self.loai = loai
        self.gia = gia
        self.trangThai = trangThai
    def hienThi(self):
        print(f"{self.ma:5} | {self.loai:10} | {self.gia} | {self.trangThai}")