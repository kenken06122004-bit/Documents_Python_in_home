"""
Nhập vào danh sách gồm 5 số nguyên, sau đó:

In ra danh sách vừa nhập.

In ra phần tử đầu, phần tử cuối, và độ dài danh sách.
"""
danhsach = [] 
n = int(input("Nhap so luong cac muc trong danh sach: "))
for i in range(n):
    so = int(input("Nhap so thu {0}: ".format(i+1)))
    danhsach.append(so)
print("Danh sach vua nhap la: ",danhsach)
if len(danhsach) > 0:
    print("Phan tu dau",danhsach[0])
    print("Phan tu cuoi",danhsach[-1])
    print("Do dai danh sach", len(danhsach))
else:
    print("Danh sach trong, khong co phan tu dau va cuoi")