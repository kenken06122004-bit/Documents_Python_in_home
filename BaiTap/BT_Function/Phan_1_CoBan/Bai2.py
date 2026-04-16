# Viết hàm in ra tổng của hai số nguyên
def checkSo(a):
    if '.' in a:
        return float(a)
    else:
        return int(a) 
def tong(a, b):
    return a + b
x = checkSo(input("Nhap gia tri x = "))
y = checkSo(input("Nhap gia tri y = "))
print("Tong cua {0} va {1} la = {2}".format(x,y,tong(x,y)))