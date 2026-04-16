class HocSinh:
    # Constructor:
    def __init__(self, hoTen, tuoi): # Hàm khởi tạo có đối
        self.hoTen = hoTen
        self.tuoi = tuoi
    def __init__(self): # Hàm khởi tạo không đối
        self.hoTen = "Chua co ten"
        self.tuoi = 0
    # Methods:
    def xuatThongTin(self):
        print("Hoc Sinh --> Ten: {0} | Tuoi: {1}".format(self.hoTen,self.tuoi))
    def nhapThongTin(self):
        self.hoTen = input("Nhap ho ten hoc sinh: ")
        self.tuoi = int(input("Nhap so tuoi: "))