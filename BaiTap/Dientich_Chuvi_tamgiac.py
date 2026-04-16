import math
print('Nhập vào độ dài 3 cạnh của tam giác: ')
a = float(input("Nhap vao a: "))
b = float(input("Nhap vao b: "))
c = float(input("Nhap vao c: "))

# Test tam giac:
if(a+b>c and a+c>b and b+c>a):
    print("Ba canh nhap vao co the tao thanh mot tam giac")
    if(a==b==c):
        print("Day la tam giac deu")
    elif((a==b and (abs(a**2 + b**2 - c**2) < 1e-3)) or (a==c and (abs(a**2 + c**2 - b**2) < 1e-3)) or (b==c and (abs(b**2 + c**2 - a**2) < 1e-3))):
        print("Day la tam giac vuong can")
    elif(a==b or a==c or b==c):
        print("Day la tam giac can")
    elif(abs(a**2 + b**2 - c**2) < 1e-3 or abs(a**2 + c**2 - b**2) < 1e-3 or abs(b**2 + c**2 - a**2) < 1e-3):
        print("Day la tam giac vuong")
    else:
        print("Day chi la tam giac thuong")
    # Dien tich va chu vi:
    print("Chu vi tam giac: p = {0} + {1} + {2} = {3}".format(a,b,c,a+b+c))
    h = float(input("Nhap chieu cao h: "))
    print("Dien tich tam giac: s = (1/2) * {0} * {1} = {2}".format(a,h,(1/2)*a*h))
else:
    print("Ba can nhap vao khong the tao thanh mot tam giac")

