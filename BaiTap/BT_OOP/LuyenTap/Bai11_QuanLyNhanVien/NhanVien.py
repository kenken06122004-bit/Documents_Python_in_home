from abc import ABC, abstractmethod
class nhanVien(ABC):
    def __init__(self,maNV="",hoTen="",luongCB=0):
        super().__init__()
        self.maNV = maNV
        self.hoTen = hoTen
        self.luongCB = luongCB
    def xuat(self):
        print(f"{self.maNV}, {self.hoTen}, {self.luongCB}, ",end="")
    def nhap(self):
        self.maNV = input("Nhap ma nhan vien: ")
        self.hoTen = input("Nhap ho ten nhan vien: ")
        try:
            self.luongCB = int(input("Nhap luong co ban: "))
        except Exception as e:
            print("Loi: ",e)
    @abstractmethod
    def tinhLuong(self):
        pass