with open("D:\\Python_in_VScode\\Data_for_luyenTap\\ghiFile_06022026.txt","a",encoding="utf-8") as f:
    while True:
        maSV = input("Nhap ma sinh vien: ")
        if maSV == "":
            break
        tenSV = input("Nhap ten sinh vien: ")
        lop = input("Nhap lop: ")
        Que = input("Nhap que quan: ")
        f.write("\t".join([maSV,tenSV,lop,Que]) + "\n") # Lưu ý: Ở đây join chỉ nhận chuỗi 
        # Join có cú pháp là: "chuỗi_ngăn_cách".join(iterable_các_chuỗi). Nếu chúng ta không dùng join có thể dùng .format
