# Tìm hiểu sâu hơn về kiểu String trong python

# 1) Chuỗi + chuỗi 
a = "Nguyễn"
b = "Văn"
c = "Phi"
d = a+" "+b+" "+c
print(d)

# 2) Chuỗi nhiều dòng:          Được viết trog ''' cmt '''
a1 = '''Nguyễn Văn Phi
Đang học đại học
Trường Đại Học Duy Tân'''
print(a1)

# 3) Nhân chuỗi:
a3 = "Em hứa sẽ làm bài tập đầy đủ\n"
a4 = a3 * 10
print(a4)

# 4) Kiểm tra chuỗi: mục đích là để chúng ta kiểm tra một chuỗi có thuộc một chuỗi khác hay không hay nói khác là tìm chuỗi con
b1 = "Xin chào Phi"
b2 = "Phi"
b3 = "Nguyễn"

if b2 in b1:
    print("Chuỗi 2 là chuỗi con của chuỗi 1")
else:
    print("Chuỗi 2 không phải là chuỗi con của chuỗi 1")

if b3 in b1:
    print("Chuỗi 3 là chuỗi con của chuỗi 1")
else:
    print("Chuỗi 3 không phải là chuỗi con của chuỗi 1")

# 5) Viết hoa chữ đầu của chuỗi:
c1 = "hôm nay, trời đẹp quá"
c1 = str.capitalize(c1)
print(c1)

# 6) Viết hoa toàn bộ chuỗi:
c2 = "hôm nay, bạn đã ăn cơm chưa nguyễn văn phi"
c2 = c2.upper()
print(c2)

# 7) Viết thường toàn bộ chuỗi: 
c2 = c2.lower()
print(c2)

# 8) Tìm và đếm số luọng chuỗi con: 
c3 = "Ngôn ngữ lập trình Python hiện nay là xu hướng. Vì vậy bạn nên học Python"
print(c3.find("Python")) # Trả về -1 nếu không tìm thấy. Ngược lại trả về vị trí đầu tiên
print(c3.count("Python")) # Trả về số lần xuất hiện từ khóa trong count

# 9) Thay thế:
c4 = "Ngôn ngữ lập trình Python hiện nay là xu hướng. Vì vậy bạn nên học Python"
c4 = c4.replace("Python","PYTHON")
print(c4)

# 10) Cắt chuỗi thành list:
lst1 = c4.split(" ") # Cắt dựa trên khoảng trắng
print(lst1)

# 11) Lấy chuỗi theo vị trí \ Lấy chuỗi con:
print(c4[0:18])