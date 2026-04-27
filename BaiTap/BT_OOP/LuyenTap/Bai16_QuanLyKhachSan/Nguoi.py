from abc import ABC, abstractmethod
class nguoi(ABC):
    def __init__(self, ma, ten):
        self.ma = ma
        self.ten = ten
    @abstractmethod
    def hienThi(self):
        pass