from abc import ABC, abstractmethod
class NV(ABC):
    def __init__(self):
        self.maNV = ""
        self.hoTen = ""
        self.luongCB = 0
    def nhap(self):
        self.maNV = input("Nhap ma nhan vien: ")
        self.hoTen = input("Nhap ho va ten: ")
        self.luongCB = int(input("Nhap luong co ban: "))
    def xuat(self):
        print("MaNV = {0} | hoTen = {1} | luongCB = {2} | ".format(self.maNV,self.hoTen,self.luongCB),end="")
    @abstractmethod
    def tinhLuong(self):
        pass