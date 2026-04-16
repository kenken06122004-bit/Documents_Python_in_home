# Yêu cầu nhập vào n > 0 nếu sai thì nhập lại
"""n = int(input("Nhập vào n: "))
while n <= 0:
    n = int(input("Nhập lại n: "))"""
# ==> Khi chúng ta không biết được số lần lặp của bài toán thì chúng ta sẽ sử dụng vòng lặp WHILE

"""a = 0
while a <= 10:
    print(a,"Bên trong WHILE")
    a += 1
else: 
    print(a,"Bên trong ELSE")""" # Nếu vòng lặp rơi vào else thì sẽ thoát vòng lặp nếu không có break trong phần body
# Trường hợp nếu có break trong while thì else sẽ không được thực thi
# Ví dụ: 
a = 0
while a <= 10:
    print(a,"Bên trong WHILE")
    a += 1
    if a >= 5:
        break  # Sau khi a tăng lên bằng 5 thì nó đi vào câu lệnh if và break ra khỏi vòng lặp
else: 
    print(a,"Bên trong ELSE")