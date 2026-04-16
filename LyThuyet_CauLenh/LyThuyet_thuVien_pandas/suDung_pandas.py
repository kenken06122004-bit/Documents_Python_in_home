import pandas as pd

with open("D:\\Python_in_VScode\\Data_for_luyenTap\\ghiFile_06022026.txt","a",encoding="utf-8") as f:
    while True:
        maSV = input("Nhap ma sinh vien: ")
        if maSV == "":
            break
        tenSV = input("Nhap ten sinh vien: ")
        lop = input("Nhap lop: ")
        Que = input("Nhap que quan: ")
        f.write("\t".join([maSV,tenSV,lop,Que]) + "\n")

# Doc File:

print("Cach 1: khong su dung pandas")
with open("D:\\Python_in_VScode\\Data_for_luyenTap\\ghiFile_06022026.txt","r",encoding="utf-8") as f:
    print("\t".join(["Ma sinh vien","Ten sinh vien","Lop","Que quan"]))
    for sv in f.readlines():
        print(sv.replace("\n",""))

print("\nCach 2: su dung pandas") # Dau tien can import thu vien pandas
f = "D:\\Python_in_VScode\\Data_for_luyenTap\\ghiFile_06022026.txt"
SV = pd.read_csv(f,sep="\t",names=["Ma sinh vien","Ten sinh vien","Lop","Que quan"])
print(SV)

# Sắp xếp theo cột: <tên_biến> = <tên của biến chứa toàn bộ dữ liệu của file>.sort_values(["tên trường cột cần sắp xếp"])

"""print("\nBang sau khi sap xep theo LOP")
ds_lop = SV.sort_values(["Lop"])
print(ds_lop)"""

# Trích rút data: <tên_biến> = <tên của biến chứa toàn bộ dữ liệu của file>.query("Điều kiện trích chọn")

svsv = SV.query('Lop == "Ba" or `Que quan` == "Ba"') # Ở đây, trường Que quan có khoảng trắng ở giữa nên pandas sẽ không hiểu, chính vì vậy
print("\nKet qua loc theo dieu kien:") # ta sẽ để những trường có khoảng trắng trong `.....` 
print(svsv)