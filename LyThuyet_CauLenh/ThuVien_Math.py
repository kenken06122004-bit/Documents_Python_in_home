import math # Phải khai báo thư viện để có thể sử dụng được các hàm trong math
def chuyen_so(x):
    if '.' in x:
        return float(x)
    else:
        return int(x)
a = chuyen_so(input("Nhap vao a: "))

# Hàm trị tuyệt đối

print("|a| = ",math.fabs(a))

# Hàm căn bậc hai

if a > 0:
    print("can hai cua a = ",math.sqrt(a))
else:
    print("a phai la gia tri lon hon khong.")

# Trả về số nguyên nhỏ nhất hoặc bằng của a nếu a là kiểu float
print("Lam tron a: ",math.ceil(a))

# Trả về số nguyên lớn nhất hoặc bằng của a nếu a là kiểu float

print("Lam tron a: ",math.floor(a))

# Và còn rất nhiều hàm khác trong math