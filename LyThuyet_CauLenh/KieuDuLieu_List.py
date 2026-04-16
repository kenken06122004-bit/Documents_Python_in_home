# Tạo list rỗng && cách khai báo một list
Rong_List = []

# Tạo ra một đối tượng list:
Rong = list() # --> list() ở đây là hàm dựng sẵn trong constructed của class list nên khi khai báo kiểu này chính là đang tạo ra một đối tượng thuộc kiểu list

# Cả hai cú pháp trên đều chưa có dữ liệu truyền vào
print(Rong_List) # --> []
print(Rong)      # --> []

# Tạo list có dữ liệu:
a = ["Xanh","Đỏ","Tím","Vàng"]
print(a)
print(a[2]) # chúng ta có thể tương tác với các dữ liệu trong list thông qua các index của nó, luôn bắt đầu từ 0. Giống mảng trong C và java
print(a[:]) # như này nó sẽ lấy ra được hết cả 4 phần từ
print(a[1:3]) # Như này nó sẽ lấy ra phần tử index 1 và 3-1 = 2
print(a[0:3])
print(a[0:4])

# Thêm dữ liệu vào list a (cuối):          Cú pháp: <Tên List> + . + append + (<Dữ liệu muốn đưa vào>)
a.append("Chàm")
print(a)

# Chèn dữ liệu vào vị trí mong muốn:        Cú pháp: <Tên list> + . + insert(<index>,<data>)
a.insert(2,"Xám")
print(a)

# Số lượng phần tử có trong list:
print(len(a))

# Đếm số lượng phần tử thỏa điều kiện:         Cú pháp: <Tên list> + . + count(<data cần đếm>)
a.append("Xanh")
a.append("Đỏ")
a.append("Vàng")
print("List a sau khi thêm: ",a)
print("Số lượng đỏ: ",a.count("Đỏ"))

# Xóa phần tử trong list: 
a.remove("Vàng") # Cú pháp này nó chỉ xóa phần tử <data truyền vào> đầu tiên mà nó gặp trong danh sách — không xóa hết.
print(a)

# Kiểm tra phần tử tồn tại hay không trong list: (in)
if "Vàng" in a:
    print("Vẫn còn vàng trong list a: ",a)
else: 
    print("Không còn vàng trong list a: ",a)

# Xóa phần tử ra khỏi list bằng vị trí: 
a.pop(7)
if "Vàng" in a:
    print("Vẫn còn vàng trong list a: ",a)
else: 
    print("Không còn vàng trong list a: ",a)

# Đảo ngược list: 
a.reverse()
print(a)

# Sắp xếp list: theo bảng chữ cái ASCII
a.sort()
print(a)
                                        # Cả hai cách sắp xếp đều cùng một cú pháp nhưng chỉ có thể sắp xếp được khi các giá 
                                        # trị phần tử trong list đều cùng một kiểu dữ liệu. Nếu khác kiểu sẽ báo lỗi
                                        # Cách xử lí: là ép kiểu về một kiểu dữ liệu duy nhất theo chuỗi hoặc theo số
# Sắp xếp list: theo số
so = [1,6,7,6,1,5,4,6,10,48,56]
so.sort()
print(so)

# Sắp xếp giảm dần >< đảo ngược list:
print("Ví dụ: ")
b = [1,5,4,6,8,7,9,6,1,2,45,6,23,4,65,3,5,6,0]
b.sort(reverse=True)                # ở đây nếu true là giảm dần, còn false là tăng dần
print(b)

# Xóa toàn bộ dữ liệu trong list:           Cú pháp: <tên list> + . + clear()
print("List sau khi xóa sạch dữ liệu: ")
a.clear()
b.clear()
so.clear()
print(a,b,so,sep="\n")