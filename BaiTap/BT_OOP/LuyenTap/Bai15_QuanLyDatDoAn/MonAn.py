from abc import ABC, abstractmethod
class MonAn(ABC):
    def __init__(self,maMon = "",tenMon = "",gia = 0):
        self.maMon = maMon
        self.tenMon = tenMon
        self.gia = gia
    def xuat(self):
        print(f"Ma mon: {self.maMon} | Ten mon: {self.tenMon} | Gia ban: {self.gia}",end=" | ")
    @abstractmethod
    def tinhGia(self):
        pass