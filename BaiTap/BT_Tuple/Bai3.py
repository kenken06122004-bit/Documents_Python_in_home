"""Tạo 2 tuple:

a = (1, 2, 3)
b = (4, 5, 6)

Ghép 2 tuple lại với nhau.

Đếm xem phần tử 5 có trong tuple ghép không."""
a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
print("Tuple ghép của a và b là: ", c)
if 5 in c:
    print("Có phần tử 5 trong Tuple ghép của a và b")