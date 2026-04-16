class people:
    def __init__(self):
        self.hoten = "none"
        self.tuoi = 0
    def nhap(self):
        self.hoten = input("Nhap ho ten: ")
        self.tuoi = int(input("Nhap so tuoi: "))
    def xuat(self):
        print("Ho ten: {0} | Tuoi: {1}".format(self.hoten,self.tuoi), end = " | ")