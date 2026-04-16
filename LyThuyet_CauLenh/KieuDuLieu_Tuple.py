""" Tuple là một chuỗi các phần tử có thứ tự giống như một List. Sự khác biệt duy nhất là bộ giá 
trị là các hằng số. Tuple một khi được tạo ra thì giá trị của nó không thể sửa đổi

Tuple được sử dụng để bảo vệ dữ liệu và thường nhanh hơn danh sách vì chúng không thể thay đổi động

Được định nghĩa trong dấu ngoặc đơn (), các mục được phân tách bằng dấu phẩy

Giá trị của Tuple có thể trùng lặp

Ví dụ:  """
gioiTinh = ("Nam","Nữ")
lopHoc = (1,2,3,4,5,6,7,8,9,10,11,12)
traiCay = ("Táo","Chuối","Táo","Cam","Mận","Dưa hấu")

# Các thao tác với Tuple:

# 1) Lấy các giá trị ở từng vị trí:

print(gioiTinh[0]) # Lấy gioiTinh vị trí số 0
print(traiCay[0:2]) # Lấy traiCay vị trí từ số 0 đến vị trí số 2 - 1 = 1 
# Lưu ý: Giá trị phần tử của Tuple là không thể thay đổi
# Ví dụ: lopHoc[0] = 13 này là sai hoàn toàn vì Tuple không thể thay đổi giá trị

# 2) Cộng hai Tuple:

y = (1,2,3) + (4,5,6)
print(y)

# 3) Nhân hai Tuple:

y2 = (1,2,3) * 2
print(y2)

# 4) Dùng In để kiểm tra phần tử có nằm trong Tuple hay không

print("Táo" in traiCay) # sẽ cho ra true hoặc false

# 5) Độ dài của Tuple:

y3 = len(traiCay)
print(y3)

# 6) Đếm số lượt xuất hiện: 

print(traiCay.count("Táo"))

# 7) Tìm max, min, sum: 

print(min(gioiTinh))
print(max(traiCay))
print(sum(lopHoc))
# Ở đây hàm min và max có thể dùng cho số hoặc cho ký tự, đáp án sẽ là ký tự lớn nhất hoặc nhỏ nhất theo aphab
# Còn hàm Sum chỉ dùng cho các giá trị số chứ không dùng cho ký tự, tính tổng của Tuple theo ASCII

# 8) Sắp xếp Tuple và chuyển về List:

listTC = sorted(traiCay)
print(listTC)