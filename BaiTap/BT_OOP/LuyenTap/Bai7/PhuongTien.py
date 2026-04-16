class Xe:
    def __init__(self):
        self.hangSX = "node"
        self.namSX = 0
    def nhap(self):
        self.hangSX = input("Nhap hang san xuat: ")
        self.namSX = int(input("Nhap nam san xuat: "))
    def xuat(self):
        print("Hang san xuat: {0} | Nam san xuat: {1}".format(self.hangSX,self.namSX), end="")