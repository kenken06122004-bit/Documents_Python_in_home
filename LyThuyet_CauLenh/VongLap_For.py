def chuyenSo(x):
    if '.' in x:
        return float(x)
    else:
        return int(x)
# Ví dụ: In các con số từ 0 đến 10
"""for i in range(10): # In i từ 0 cho đến 10 - 1 = 9 
    print(i)"""

# Ví dụ: tính tổng các số từ 0 đến 10 
"""tong = 0
for i in range(10): # In i từ 0 cho đến 10 - 1 = 9 
    tong = tong + i
print("Tổng các số từ 0 đến 9 là: ",tong)"""

# Ví dụ: tính tổng các số từ 0 đến n (tính luôn cả n)
"""n = chuyenSo(input("Nhap vao n: ")) # input đều cho ra kiểu String nên phải ép kiểu
tong = 0
for i in range(n+1): # In i từ 0 cho đến (n+1) - 1 = n 
    tong = tong + i
print("Tổng các số từ 0 đến",n,"la:",tong)"""

# Ví dụ tính tổng số chắn từ 0 đến n (tính luôn cả n)
    # Cách 1: dùng bước nhảy
"""n = chuyenSo(input("Nhap n: "))
tongChan = 0
for i in range(0,n+1,2): # có nghĩa là chạy từ 0 đến n và mỗi lần nhảy 2 đơn vị
    tongChan = tongChan + i
print("Tổng các số chắn từ 0 đến",n,"là:",tongChan)"""
    # Cách 2: dùng if
"""n = chuyenSo(input("Nhap n: "))
tongChan = 0
for i in range(n+1):
    if i%2==0:
        print(i)
        tongChan = tongChan + i
print("Tổng các số chẵn từ 0 đến",n,"là:",tongChan)"""

# Tính tổng các giá trị trong mảng
n = chuyenSo(input("Nhập số lượng phần tử: "))
ds = [] # Rỗng
for i in range(n):
    x = input("Nhập phần tử thứ "+str(i+1)+" bằng: ") # Trong print thì ta dùng , còn trong input ta dùng +
    ds.append(x) # Thêm x là danh sách mảng
    #ds.append(chuyenSo(x)) nếu ta dùng như thế này tức là ta sẽ chuyển đổi kiểu dữ liệu cho x khi thêm vào 
    # danh sách ngay sau khi nhập nhưng vậy ta sẽ đỡ gọi lại hàm chuyển số dưới tính tổng và tính lẻ
print("Danh sách vừa nhập là: ",ds)
tongChan = 0
tongLe = 0
for i in ds:
    if chuyenSo(i) % 2 == 0:
        tongChan += chuyenSo(i)
    else:
        tongLe += chuyenSo(i)
print("Tổng các số lẻ trong ds là:",tongLe)
print("Tổng các số chẵn trong ds là:",tongChan)