"""Cho danh sách:

ds = ["apple", "banana", "cherry", "apple", "orange", "banana"]

Xóa các phần tử trùng lặp.

In ra danh sách mới không trùng."""
ds = ["apple", "banana", "cherry", "apple", "orange", "banana"]
# Khai báo một List rỗng để chứa các phần tử duy nhất (không trùng lặp của ds):
ds_khong_trung = []
# Dùng vòng lặp for để kiểm tra, nếu có trong ds_khong_trung thì bỏ qua ngược lại thì thêm vào
for i in ds:
    if i not in ds_khong_trung:
        ds_khong_trung.append(i)
print(ds_khong_trung)