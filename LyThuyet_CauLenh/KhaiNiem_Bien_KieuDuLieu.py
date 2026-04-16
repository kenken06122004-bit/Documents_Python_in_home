""" Trong python, chúng ta không cần phải khai báo biến cũng như chỉ rõ kiểu dữ liệu của biến đó, biến sẽ được tạo và xác định
kiểu tự động (dynamic typing) khi bạn gán giá trị cho nó
Để viết kiểu dữ liệu của biến chúng ta có thể sử dụng hàm type() """
# Vd:
a = 100
print(type(a)) # Kết quả nó sẽ ra: <class 'int'> tức là kiểu dữ liệu int
""" Chú ý: 
1) Không được đặt tên biến có chứa dấu cách, kí tự đặc biệt, bắt đầu bằng chữ số
2) Tên biến trong python phân biệt hoa thường """
# Ngoài ra chúng ta có thể đặt và gán giá cho nhiều biến cùng một lúc
# Ví dụ:
x, y, z = 1 , 2 , "Văn Phi"
print(x,y,z,sep=", ")
# Thêm nữa, trong python còn hỗ trợ cho chúng ta gán được giá trị giống nhau cho nhiều biến
# Ví du:
b = c = d = 10
print(b,c,d)

""" Về hằng số, thì trong python chúng ta sẽ không có hằng số, thường thì chúng ta sẽ biểu diễn hằng số theo hai cách: """
# Cách 1: 
PI = 3.14 # tức là chúng ta đã gán 3.14 cho PI và trong python chúng ta sẽ ngầm hiểu rằng các biến được IN HOA sẽ là
          # các hằng số và hạn chế thay đổi chúng
# Cách 2: 
import math
print(math.pi) # Đây là cách chúng ta lấy giá trị hằng số đã được khai báo sẵn trong python và chúng ta cũng có thể thay đổi
               # giá trị của nó. Tuy nhiên, chúng ta sẽ hạn chế thay đổi các hằng số này

""" Trong python, chúng ta sẽ có 5 kiểu dữ liệu: """

""" Kiểu dữ liệu số nguyên (int): """
# 1) Không giới hạn về giá trị, có thể lưu số lớn
# 2) Trong python thì các số nguyên thường được in ra dưới dạng cơ số 10, nhưng cũng thể in ra các số ở hệ 2, 8, 16
# Ví dụ:
# a) Ví dụ về hệ cơ số 10: 
m = 10
print(" m = {0}".format(m))
# b) Ví dụ về hệ cơ số 2: Bắt đầu bằng 0b hoặc 0B
n = 0b1010
print(" n = {0}".format(n))
# c) Ví dụ về hệ cơ số 8: Bắt đầu bằng 0o hoặc 0O
v = 0o12
print(" v = {0}".format(v))
# d) Ví dụ về hệ cơ số 16: Bắt đầu bằng 0x hoặc 0X
p = 0xA
print(" p = {0}".format(p))

""" Kiểu số thực: """
# Số thực là số âm - dương kèm theo phần thập phân
# Trong python giá trị số thực có thể lưu lớn nhất xấp xỉ 1.8 x 10 ^ 308 nếu lớn hơn chuỗi đó thì giá trị sẽ là infinity và 
# giá trị số thực nhỏ nhất có thể lưu là 5.0 x 10 ^ -324 nếu nhỏ hơn chuỗi đó thì giá trị sẽ là 0
# Ví dụ:
u = 3.5 
print(" u = {0}".format(u))

io = 3e5 # có nghĩa là 3.10^5
print(" io = {0}".format(io))

ia = 1.9e308
print(" ia = {0}".format(ia))

ib = 5.1e-325
print(" ib = {0}".format(ib))
# In số thực với lượng chữ số sau dấu , xác định
# Ví dụ: 
im = 28.0412323
# cách 1: 
print('%.2f'%im)
# cách 2: nguy hiểm dễ làm tròn số
print(round(im,2))
# cách 3: 
print('{:.2f}'.format(im))

""" Kiểu số phức """
# Số phức gồm: phần thực (real part) và phần ảo (imaginary part)
# Chúng ta có thể xuất phần thực và phần ảo của số phức bằng cách: 
po = (3 + 5j) 
print(po.real)
print(po.imag)

""" Kiểu đúng - sai """
# Kiểu bool chỉ lưu 2 giá trị true và false
# Chú ý: Các giá trị được xác định là true trong python: xâu khác rỗng (nếu có dấu cách thì nó vẫn là true) và số khác 0
# Ví dụ: 
print(bool(100))
print(bool(0))
print(bool("Hello"))
print(bool(""))