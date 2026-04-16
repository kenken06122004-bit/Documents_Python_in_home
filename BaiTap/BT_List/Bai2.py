"""
Nhập vào danh sách các số nguyên.

In ra danh sách theo thứ tự tăng dần.

In ra phần tử lớn nhất và nhỏ nhất.
"""
ds = []
n = int(input("Nhập vào số lượng phần tử của List: "))
for i in range(n):
    so = int(input("Nhập phần tử thứ {0}: ".format(i+1)))
    ds.append(so)
print("Danh sách vừa nhập là: ", ds)
ds.sort()
print("Sắp xếp danh sách theo thứ tự tăng dần là: ",ds)
ds.sort(reverse=True)
print("Sắp xếp danh sách giảm dần: ",ds)
print("Phần tử lớn nhất: ", max(ds))
print("Phần tử nhỏ nhất: ", min(ds))
