"""Viết chương trình cho phép nhập danh sách 5 số, sau đó tính:

Tổng, trung bình, và số lượng phần tử chia hết cho 2."""
ds = []
n = int(input("Nhập số lượng phần tử cho danh sách: "))
for i in range(n):
    so = int(input("Nhập phần từ thứ {0}: ".format(i+1)))
    ds.append(so)
print("Danh sách vừa nhập là: ",ds)
print("Tổng của danh sách vừa nhập là: ",sum(ds))
print("Trung bình danh sách vừa nhập là: ",(sum(ds)/len(ds)))
print("Các phần tử chia hết cho 2 là: ")
for i in ds:
    if i % 2 == 0:
        print(i)