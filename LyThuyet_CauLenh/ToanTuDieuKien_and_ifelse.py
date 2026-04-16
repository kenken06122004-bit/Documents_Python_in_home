# Câu lệnh điều kiện - Toán tử ba ngôi
# Cú pháp: [Trả về khi đúng điều kiện] if [điều kiện] else [Trả về khi sai điều kiện]

x = "Đúng" if 5>3 else "Sai"
print(x)

y = int(input("Nhập vào một số nguyên: "))
kq = "Chẵn" if (y%2==0) else "Lẻ"
print(y,"là số ",kq)

# Câu lệnh rẽ nhánh: if else
# Cú pháp: 
#          if[<Điều kiện>]:
#                [<Câu lệnh>] 
#          else: 
#                [<Câu lệnh>] 

z = int(input("Nhập vào z: "))
if z>0: 
    print(z,"là số dương")
else:
    print(z,"là số âm")
