# Viết hàm check chan le:
def checkSo(x):
    if '.' in x:
        return float(x)
    else:
        return int(x)
def checkChanLe(x):
    if x % 2 == 0:
        print(x,"la so chan")
    else: 
        print(x,"la so le")
while True:
    try:
        a = checkSo(input("Nhap so nguyen n = "))
        break 
    except ValueError:
        print("Loi, vui long nhap lai")
checkChanLe(a)      