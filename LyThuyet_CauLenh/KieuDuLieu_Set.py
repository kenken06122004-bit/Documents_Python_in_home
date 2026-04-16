""" - Set là một trong 4 kiểu dữ liệu tích hợp sẵn trong Python dùng để lưu trữ các tập hợp dữ liệu
3 kiểu còn lại là List[], Tuple() và Dictionary{}, tất cả đều có chất lượng và cách sưe dụng khác 
nhau

- Set là tập hợp không có thứ tự , giá trị không được trùng nhau, không thể thay đổi và không lập chỉ mục. Lưu ý: Các mục set là không thể thay
đổi, nhưng bạn có thể xóa các mục và thêm các mục mới

- Sử dụng cặp ngoặc {}

Đặc điểm	Mô tả
📦 Không trùng lặp	                Mỗi giá trị chỉ xuất hiện 1 lần
🔢 Không có chỉ số	                Không truy cập bằng set[0]
🧮 Có thể thêm / xóa phần tử	    Dùng .add() và .remove()
⚡ Tốc độ tìm kiếm nhanh	           Nhanh hơn list khi kiểm tra in"""

# Tạo mới set
monHoc = {"Toán","Lý","Hóa"}
print(monHoc)

# Duyệt từng phần tử trong set:
for x in monHoc:
    print(x)

# Thêm phần tử vào bên trong set:
monHoc.add("Lịch sử")           # add chỉ dùng để thêm 1 phần tử vào set
print(monHoc)

hocThem = {"Anh văn","Đàn Piano"} # update dùng để thêm nhiều phần tử vào set
monHoc.update(hocThem)
print(monHoc)

# Thêm List vào Set:   # Tương tự cho Tuple và Dictionary
hocPhuDao = ["Võ thuật","Múa","Võ thuật"]
print(hocPhuDao)
monHoc.update(hocPhuDao)  # Tuy là trong List có trùng phần tử nhưng khi truyền vào set và in ra thì chỉ có một thôi
print(monHoc)

# Xóa:
monHoc.remove("Võ thuật")
print(monHoc)       # Nếu không tìm thấy để xóa thì chương trình sẽ báo lỗi 

monHoc.discard("Toán")
print(monHoc)       # Còn discard nếu có thì xóa không thì thôi chứ không báo lỗi

# Xóa phần tử đầu tiên (Ngẫu nhiên vì set không có thứ tự nên chương trình sẽ xóa ngẫu nhiên):
monHoc.pop()
print(monHoc)

# Xóa hết toàn bộ:
monHoc.clear()  # Xóa hết dữ liệu trong set
print(monHoc)

del monHoc  # Xóa luôn cả set kể cả dữ liệu khi đó in ra sẽ bị lỗi
print(monHoc)