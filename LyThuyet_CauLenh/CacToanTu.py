# Phép toán cơ số:
"""""
print("Nhập vào số a: ")
a = int(input())
print("Nhập vào số b: ")
b = int(input())
print("{0}+{1}={2}".format(a,b,a+b)) # a cộng b
print("{0}-{1}={2}".format(a,b,a-b)) # a trừ b
print("{0}*{1}={2}".format(a,b,a*b)) # a nhân b
print("{0}/{1}={2}".format(a,b,a/b)) # chia thập phân
print("{0}//{1}={2}".format(a,b,a//b)) # chia lấy nguyên
print("{0}%{1}={2}".format(a,b,a%b)) # chia lấy dư
print("{0}**{1}={2}".format(a,b,a**b)) # mũ lũy thừa (a mũ b) 
"""""
# Phép toán so sánh:
"""""
def chuyen_so(x):
    if '.' in x:
        return float(x)
    else:
        return int(x)
x = chuyen_so(input("Nhập vào x: "))
y = chuyen_so(input("Nhập vào y: "))
print("{0}>{1} là {2}".format(x,y,x>y)) 
print("{0}<{1} là {2}".format(x,y,x<y)) 
print("{0}=={1} là {2}".format(x,y,x==y)) 
print("{0}!={1} là {2}".format(x,y,x!=y)) 
print("{0}>={1} là {2}".format(x,y,x>=y)) 
print("{0}<={1} là {2}".format(x,y,x<=y)) 
"""
# Phép toán logic: 
"""""
z = chuyen_so(input("Nhập vào z: "))
print("{0} > {1} and {2} > {3} = {4}".format(x,y,y,z, x > y and y > z))
print("{0} < {1} or {2} < {3} = {4}".format(x,y,y,z, x < y or y < z))
print("not({0}>{1}) = {2}".format(x,z, not(x>z)))
"""""
# Toán tử gán:
"""""
# a = b (Cú pháp)
# Ví dụ: 
a1 = 1000
b1 = a1
print(b1)
# Ngoài ra ta có thể gán trên 1 dòng: 
a2, a3, a4 = 5, 10, 15
print(a2)
print(a3)
print(a4)
# Lưu ý: Hoán vị GT của 2 biến
a1, a2 = a2, a1
print(a1,a2) """""

