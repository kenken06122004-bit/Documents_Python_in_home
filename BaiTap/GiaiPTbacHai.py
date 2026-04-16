print("Nhập vào 3 số của phương trình bậc hai như sau: ax^2 + bx + c = 0")
import math
def chuyen_so(x):
    if '.' in x:
        return float(x)
    else:
        return int(x)
a = chuyen_so(input("Nhập vào a: "))
b = chuyen_so(input("Nhập vào b: "))
c = chuyen_so(input("Nhập vào c: "))
if a!=0:
    print("Phương trình bậc hai ta có là: {0}x^2 + {1}x + {2} = 0".format(a,b,c))
else:
    print("Đây không phải là phương trình bậc hai")
print("Tính denta: ")
denta = math.pow(b,2) - 4 * a * c
if denta < 0:
    print("Phuong trinh vo nghiem")
elif denta == 0: # Đây là cách viết tắt else-if
    print("Phuong trinh co hai nghiem bang nhau: ")
    print("x1 = x2 = {0}".format((-b)/(2*a)))
else:
    print("Phuong trinh co hai nghiem phan biet: ")
    print("x1 = {0} va x2 = {1}".format((-b-math.sqrt(denta))/(2*a),(-b+math.sqrt(denta))/(2*a)))