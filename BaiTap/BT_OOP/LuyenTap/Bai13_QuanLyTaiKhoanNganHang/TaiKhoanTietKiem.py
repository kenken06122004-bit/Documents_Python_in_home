from TaiKhoan import TaiKhoan
class taiKhoanTietKiem(TaiKhoan):
    def __init__(self, soTK="", tenChuTK="", soDu=0, laiSuat = 0.05):
        super().__init__(soTK, tenChuTK, soDu)
        self.laiSuat = laiSuat
    def tinhLaiHoacPhi(self):
        return self.soDu * self.laiSuat
    def xuat(self):
        super().xuat()
        print(f"LaiSuat = {self.laiSuat*100}% | Lai = {self.tinhLaiHoacPhi()}")