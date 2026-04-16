from abc import ABC, abstractmethod
class TaiKhoan(ABC):
    def __init__(self, soTK = "", tenChuTK = "", soDu = 0):
        self.soTK = soTK
        self.tenChuTK = tenChuTK
        self.soDu = soDu
    def guiTien(self):
        try:
            soTien = int(input("Nhap so tien gui: "))
        except Exception as e:
            print("Loi: ", e)
        else:
            if soTien > 0:
                self.soDu += soTien
                print(f"Da gui {soTien}VND vao tai khoan.")
            else: 
                print("So tien gui khong hop le")
    def rutTien(self):
        try:
            soTienCanRut = int(input("Nhap so tien can rut"))
        except Exception as e:
            print("Loi: ", e)
        else:
            if soTienCanRut > self.soDu:
                print("So du khong du")
            elif soTienCanRut <= 0:
                print("So tien rut khong hop le")
            else:
                self.soDu = self.soDu - soTienCanRut
                print(f"Rut thanh cong {soTienCanRut}. So du hien tai: {self.soDu}")
    @abstractmethod
    def tinhLaiHoacPhi(self):
        pass   
    def xuat(self):
        print(f"SoTK = {self.soTK} | tenChuTK = {self.tenChuTK} | soDu = {self.soDu}",end=" | ")   