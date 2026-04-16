# Viết hàm tính bình phương của một số:
def checkSo(x):
    if '.' in x:
        return float(x)
    else:
        return int(x)
def binhPhuong(x):
    return x * x
a = checkSo(input("Nhap gia tri x = "))
print("Binh phuong cua {0} = {1}".format(a,binhPhuong(a)))