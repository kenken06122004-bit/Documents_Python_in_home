"""
- Kiểu dữ liệu Dictionary là kiểu dữ liệu lưu trữ theo cặp key - value
- Mỗi key ánh xạ đến một value, giống như cách chúng ta tra nghĩa trong từ điển
"""
# Ví dụ: 
sinh_vien = {
    "Ho va ten" : "Nguyễn Văn Phi",
    "Tuổi" : "22",
    "Lớp" : "Khoa học dữ liệu"
}
# Ở đây "Họ và tên" , " Tuổi" , "Lớp" chính là key
# Còn bên phải dấu : chính là các value và mỗi key đều có một value
# Để mà chúng ta truy xuất tới dữ liệu bên trong, thì: 

print(sinh_vien["Ho va ten"])

# Chúng ta chỉ sử dụng tên key để truy xuất tới, và nếu key không tồn tại thì chương 
# trình sẽ báo lỗi KeyError
# Và để tránh lỗi chúng ta sẽ dùng phương thức get():

print(sinh_vien.get("Ho va ten","Không có dữ liệu"))
print(sinh_vien.get("Nganh hoc","Không có dữ liệu"))

# 1) Thay đổi dữ liệu: 

# Cách 1:
sinh_vien["Lớp"] = "K30 - TKD"
print(sinh_vien["Lớp"])
# Cách 2:
sinh_vien.update({"Ho va ten" : "Van Phi"})
print(sinh_vien["Ho va ten"])
# Ở cách 2 này chúng ta có thể thay đổi nhiều key cùng một lúc
sinh_vien.update({"Ho va ten" : "Phi", "Lớp" : "K30"})
print(sinh_vien["Ho va ten"])
print(sinh_vien["Lớp"])

print(sinh_vien)

# 2) Thêm dữ liệu: thêm mới cả key và value nếu:

# Cách 1: 
sinh_vien["Ten ban be hoac dong nghiep"] = "Tran Hoang Nhat Nam"
print(sinh_vien)
# Cách 2: 
sinh_vien.update({"Nganh hoc" : "CNTT - Khoa hoc du lieu"})
print(sinh_vien)

""" Lưu ý: Rằng việc thêm và cập nhật hay sửa dữ liệu bên trong một dictionary đều có các cú pháp giống nhau, nhưng để
thêm được dữ liệu mới thì ta phải thêm key mới nếu ta sài key cũ thì nó sẽ chỉ đè lên dữ liệu cũ của key đó"""

# 3) Xóa dữ liệu: 

# Cách 1: xóa theo key chỉ định
sinh_vien.pop("Lớp")
print(sinh_vien)
# Cách 2: Xóa cặp key - value cuối cùng
sinh_vien.popitem()
print(sinh_vien)
# Cách 3: Xóa theo key chỉ định
del sinh_vien["Tuổi"]
print(sinh_vien)
""" Lưu ý: ở cách 3 xóa phần tử nêu chúng ta chỉ gõ del sinh_vien mà không truyền vào key thì nó sẽ xóa hoàn toàn dữ liệu trong sinh_vien"""

""" Tạo mới lại sinh viên để thực hành không liên quan đến bài học"""
sinh_vien1 = {"Hoten" : "Nguyen Van Phi", "Lop" : "K30", "Ngay/thang/nam sinh" : "06/12/2004", "Tuoi" : 22, "Nganh hoc" : "Khoa hoc du lieu"}
print(sinh_vien1)

# 4) Xóa toàn bộ dữ liệu trong một đối tượng

#sinh_vien1.clear()
#print(sinh_vien1)

# 5) Chỉ lấy dữ liệu key hoặc value :

# Duyệt các giá trị của keys:
for x in sinh_vien1.keys():
    print(x)

print("\n")

# Duyệt các giá trị của value:
for x in sinh_vien1.values():
    print(x)

# 6) Lấy theo cặp key - value:

for x, y in sinh_vien1.items():
    print(x,":",y)