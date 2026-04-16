"""Định nghĩa:
- Hàm là một khối mã chỉ chạy khi nó được gọi
- Bạn có thể truyền dữ liệu, được gọi là tham số, vào một hàm
- Kết quả là một hàm có thể trả về dữ liệu

- Ví dụ: khai báo hàm
def xinChao():
    print("Xin chào")
"""
def xinChao(hoVaTen):  # Hàm có thể nhận nhiều đối số không bị giới hạn
    print("Xin chào " + hoVaTen)
xinChao("Nguyễn Văn Phi")

def xinChaoBan(ho, lot, ten):
    print("Xin chào", ho, lot, ten)
xinChaoBan("Nguyễn","văn","Fi")

# Lưu ý: nếu dùng dấu , để nối chuỗi thì ta không cần ép kiểu khi có số và Python sẽ tự thêm khoảng trắng đầu và cuối chuỗi cho ta
def xx(tuoi):
    print("Xin chào, năm nay tôi",tuoi,"tuổi")
xx(22)
# Ngược lại nếu dùng dấu + thì ta phải ép kiểu và cộng khoảng trắng
def yy(tuoi):
    print("Xin chào, năm nay tôi " + str(tuoi) + " tuổi")
yy(22)

# Khi không xác định được đối số, chúng ta có thể sử dụng dấu *
def thoiKhoaBieu(*monHoc):
    print("Môn 1:", monHoc[0])
    print("Môn 2:",monHoc[1])
thoiKhoaBieu("Toán","Lý","Hóa","Sinh","Sử") # Ở đây nó sẽ chỉ in ra hai môn đầu đó là Toán và Lý vì chúng ta chỉ lấy 0 và 1
# Khi cần lấy hết
def tinhTong(*giaTri): # Lưu ý: * này khác với List
    sum = 0
    for x in giaTri:
        sum += x
    print(sum)
tinhTong(1,2,3,4,5,6,7,8,9) # Python rất linh động hơn các ngôn ngữ lập trình khác. Thay vì chúng ta phải thêm vào mảng list v.v thì ta có thể đưa thẳng đối số của hàm

# Truyền nhiều đối số, xác định thông qua tên, sử dụng **
def xinChao1(**hoVaTen):
    print("Xin chào:",hoVaTen["ho"]) # Ở đây bắt buộc phải có "<tên biến>"
xinChao1(ten = "Tùng", chuLt = "Nhật", ho = "Lê") # Tên biến thì không có ""

# Sủ dụng return để trả về giá trị
def tinhTich(*giaTri):
    tich = 1
    for x in giaTri:
        tich *= x
    return tich
tinhTich(1,4,6) # Không in ra giá trị nhưng nó chỉ tính trong chương trình và để lấy ra hay gọi là in ra màn hình thì như sau:
tongTich = tinhTich(1,4,6)
print(tongTich)
