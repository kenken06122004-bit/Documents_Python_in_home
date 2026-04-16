# Tìm max của 3 số nguyen nhập vào từ bàn phím:
def checkSo(x):
    if '.' in x:
        return float(x)
    else:
        return int(x)
def maxBaSo(x,y,z):
    return max(x,y,z)
def nhapSoNguyen(thong_bao):
    while True:
        try:
            return int(input(thong_bao))
        except ValueError:
            print("Loi, vui long nhap lai")
a = nhapSoNguyen("Nhap so a = ")
b = nhapSoNguyen("Nhap so b = ")
c = nhapSoNguyen("Nhap so c = ")
print("So lon nhat trong {0} va {1} va {2} la {3}".format(a,b,c,maxBaSo(a,b,c)))