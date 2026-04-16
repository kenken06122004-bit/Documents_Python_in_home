# Viết hàm dem_so_chan(lst) trả về số lượng phần tử chẵn trong danh sách lst
def demSoChan(danhSach):
    dem = 0
    for x in danhSach:
        if x % 2 == 0:
            dem += 1
    return dem
def nhapList_SoNguyen():
    n = int(input("Nhap so phan tu cua mang: "))
    danhSach = []
    for i in range(n):
        while True:
            try:
                x = int(input("Nhap phan tu thu {0}: ".format(i+1)))
                danhSach.append(x)
                break
            except ValueError:
                print("Loi, vui long nhap lai")
    return danhSach
def checkChanLe(danhSach):
    demLe = 0
    demChan = 0
    for x in danhSach:
        if x % 2 == 0:
            demChan += 1
        else:
            demLe += 1
    print("So phan tu chan trong danh sach la:", demChan)
    print("So phan tu le trong danh sach la:", demLe)
ds = nhapList_SoNguyen()
print("Mang ban vua nhap la",ds)
checkChanLe(ds)
