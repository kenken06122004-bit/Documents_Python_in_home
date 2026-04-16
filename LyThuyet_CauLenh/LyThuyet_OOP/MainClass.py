from LyThuyet import SimpleClass
from LyThuyet2 import SimpleClass2
objectA = SimpleClass()
objectB = SimpleClass()
objectA.printMe()
print(objectB.i)
# Thay đổi giá trị cảu thuộc tính
objectA.i = 100
objectB.j = 500
print(objectA.i)
objectB.printMe()
# Chúng ta không được phép lấy ra các phương thức trong class
# ví dụ: SimpleClass.printMe() --> sẽ báo lỗi
objectC = SimpleClass2()
objectD = SimpleClass2()
objectC.hello()
objectC.hi("Peter")
## Lưu ý: phương thức static không cần tạo đối tượng để gọi thì nó vẫn có thể sử dụng, thay vào đó có thể
# dùng tên class để gọi