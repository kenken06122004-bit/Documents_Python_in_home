"""Tạo một tuple chứa các số nguyên từ 1 đến 10, rồi:

In ra các phần tử chẵn.

Tính tổng các phần tử trong tuple."""
soNguyen = (1,2,3,4,5,6,7,8,9,10)
print("Các phần tử chẵn trong Tuple là: ")
for x in soNguyen:
    if x % 2 == 0:
        print(x,end = " ")