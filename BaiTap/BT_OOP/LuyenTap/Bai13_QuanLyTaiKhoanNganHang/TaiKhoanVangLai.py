from TaiKhoan import TaiKhoan
class taiKhoanVangLai(TaiKhoan):
    def __init__(self, soTK="", tenChuTK="", soDu=0, phiDuyTri = 50000):
        super().__init__(soTK, tenChuTK, soDu)
        self.phiDuyTri = phiDuyTri
    def tinhLaiHoacPhi(self):
        return self.phiDuyTri
    def xuat(self):
        super().xuat()
        print(f"phiDuyTri = {self.phiDuyTri}")