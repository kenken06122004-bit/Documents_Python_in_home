from DanhSachSanPham import DanhSachSP
ds = DanhSachSP()
n = int(input("Nhap so luong san pham: "))
for i in range(n):
    print("\n ==== Nhap san pham thu {0} ====".format(i+1))
    ds.them()
ds.xuatDanhSach()
print("====== SAN PHAM CO GIA BAN LON NHAT ======")
spMax = ds.timGiaCaoNhat()
if spMax == 0:
    print("Danh sach rong, khong co san pham")
else:
    spMax.xuat()