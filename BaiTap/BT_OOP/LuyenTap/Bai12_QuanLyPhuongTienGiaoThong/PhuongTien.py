from abc import ABC, abstractmethod
class PhuongTien(ABC):
    def __init__(self,maPT="",hangSX="",gia=0,namSX=0):
        super().__init__()
        self.maPT = maPT
        self.hangSX = hangSX
        self.gia = gia
        self.namSX = namSX
    @abstractmethod
    def tinhThue(self):
        pass
    def xuat(self):
        print(f"maPT = {self.maPT} | hangSX = {self.hangSX} | gia = {self.gia} | namSX = {self.namSX}",end=" | ")
