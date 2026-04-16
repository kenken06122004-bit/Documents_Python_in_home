"""
Xây dựng một từ điển, có các chức năng sau (người dùng lựa chọn chức năng thông qua menu):
1) Thêm một từ vựng mới (kèm nghĩa của từ vựng) vào từ điển
2) Tra cứu ý nghĩa của một từ vựng
3) Cập nhật ý nghĩa cho một từ vựng
4) Cho phép người dùng xóa đi một từ vựng trong từ điển
5) Cho phép người dùng xóa toàn bộ từ vựng trong từ điển
6) Cho phép người dùng in ra toàn bộ từ vựng
7) Cho phép người dùng in ra toàn bộ từ điển theo cấu trúc: "Từ vựng" = "Ý nghĩa"
8) Kết thúc chương trình
"""
tuDien = {} # khai báo từ điển
while(True): 
    print("Nhap: 1 = Thêm từ vựng mới | 2 = Tra cứu / tìm | 3 = Cập nhật / thêm | 4 = Xóa đi một từ | 5 = Xóa toàn bộ | 6 = In ra toàn bộ | 7 = In theo cấu trúc | 8 = Kết thúc chương trình")
    luaChon = int(input("Nhập số lựa chọn của bạn: "))
    match luaChon:
        case 1 | 3: # ở đây có thêm 3 vì nhập và cập nhật đều có cú pháp giống nhau
            tuVung = input("Nhập vào từ vựng: ")
            yNghia = input("Nhập vào ý nghĩa: ")
            tuDien.update({tuVung : yNghia}) 
            print("Nhập thành công")
        case 2: 
            tuVung = input("Nhập vào từ vựng cần tra: ")
            print("Ý nghĩa: ", tuDien.get(tuVung,"Không tìm thấy từ vựng này"))
        case 4: 
            tuVung = input("Nhập vào từ vựng cần xóa: ")
            if tuVung in tuDien:
                tuDien.pop(tuVung)
                print("Xóa thành công")
            else: 
                print("Không tìm thấy để xóa")
        case 5: 
            tuDien.clear()
            print("Xóa toàn bộ thành công")       
        case 6: 
            print("Danh sách các từ vựng có trong từ điển")
            for x in tuDien.keys():
                print(x)     
        case 7: 
            print("Danh sách các từ vựng và ý nghĩa có trong từ điển")
            for x, y in tuDien.items():
                print(x,"=",y)   
        case 8: 
            break
        case _:
            print("Chỉ nhập từ 1 - 8")  