"""Một hàm lambda là một hàm ẩn danh nhỏ
Một hàm lambda có thể nhận bất kỳ số lượng đối số nào, nhưng chỉ có thể
có một biểu thức
- Cú pháp lambda arguments : expression
- Ví dụ: """
kiemTraSoChan = lambda a : (a%2==0)
print(kiemTraSoChan(5))
#Ví dụ về sử dụng lambda function bên trong các function"
def hamMuHai(a):
    return a**2
def hamMuBa(a):
    return a**3
### 
def hamMu(n):
    return lambda x : (x**n)
hamMu2 = hamMu(2)
hamMu3 = hamMu(3)
hamMu4 = hamMu(4)
print(hamMu2(3))
print(hamMu3(3))
print(hamMu4(3))