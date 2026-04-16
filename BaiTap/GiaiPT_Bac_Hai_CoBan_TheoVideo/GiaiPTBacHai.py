# Nhâp dữ liệu: 
print("Giai phuong trinh bac hai ax^2 + bx + c = 0")
def chuyen_so(x):
    if("." in x):
        return float(x)
    else: 
        return int(x)
print("Nhap du lieu: ")
a = chuyen_so(input("Nhap a: "))
b = chuyen_so(input("Nhap b: "))
c = chuyen_so(input("Nhap c: "))
import math
if a != 0:
    denta = math.pow(b,2) - 4 * a * c
    if(denta < 0):
        print("Phuong trinh vo nghiem")
    elif(denta == 0):
        x1 = - b / (2 * a)
        print("Phuong trinh co nghiem kep: x1 = x2 = {0}".format(x1))
    else:
        x1 = (-b+math.sqrt(denta))/(2*a)
        x2 = (-b-math.sqrt(denta))/(2*a)
        print("Phuong trinh co hai nghiem phan biet: x1 = {0} va x2 = {1}".format(x1,x2))
else:
    print("Khong phai la phuong trinh bac hai")