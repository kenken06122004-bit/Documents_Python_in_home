from abc import ABC, abstractmethod
class Sach(ABC):
    def __init__(self, maSach = "", tenSach = "", tacGia = "", gia = 0):
        self.maSach = maSach
        self.tenSach = tenSach
        self.tacGia = tacGia
        self.gia = gia
    def hienThi(self):
        print(f"maSach = {self.maSach} | tenSach = {self.tenSach} | tacGia = {self.tacGia} | gia = {self.gia}", end=" | ")
    @abstractmethod
    def tinhGiaSauThue(self):
        pass
        