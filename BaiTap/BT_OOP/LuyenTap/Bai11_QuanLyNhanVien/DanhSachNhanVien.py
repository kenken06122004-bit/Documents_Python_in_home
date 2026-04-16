from NhanVien import nhanVien
from NhanVien_VP import nhanVien_VP
from NhanVien_SX import nhanVien_SX
class danhSachNV():
    def __init__(self):
        self.dsNhanVien: list[nhanVien] = []
    def docFile(self):
        try:
            with open("docFile.txt","r",encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line == "":
                        continue
                    arr = line.split(",")
                    loaiNV = arr[0]
                    maNV = arr[1]
                    hoTen = arr[2]
                    luongCB = int(arr[3])
                    if arr[0].startswith("VP"):
                        soNgayLamViec = int(arr[4])
                        newNhanVien = nhanVien_VP(maNV,hoTen,luongCB,soNgayLamViec)
                        self.dsNhanVien.append(newNhanVien)
                    elif arr[0].startswith("SX"):
                        soSanPham = int(arr[4])
                        newNhanVien = nhanVien_SX(maNV,hoTen,luongCB,soSanPham)
                        self.dsNhanVien.append(newNhanVien)
        except Exception as e:
            print("Loi doc file: ",e)
        else:
            print("Doc file thanh cong")
    def ghiFile(self):
        if not self.dsNhanVien:
            print("Danh sach rong")
            return
        try:
            with open("D:\\Python_in_VScode\\Data_for_luyenTap\\ghiFile_16022026.txt","w",encoding="utf-8") as f:
                for x in self.dsNhanVien:
                    if isinstance(x,nhanVien_SX):
                        f.write(f"{x.maNV}, {x.hoTen}, {x.luongCB}, {x.soSanPham}\n")
                    elif isinstance(x,nhanVien_VP):
                        f.write(f"{x.maNV}, {x.hoTen}, {x.luongCB}, {x.soNgayLam}\n")
        except Exception as e:
            print("Loi: ",e)
        else:
            print("Ghi file thanh cong")
    def xuat(self):
        if not self.dsNhanVien:
            print("Danh sach rong")
            return
        print("====== DANH SACH NHAN VIEN ======")
        for x in self.dsNhanVien:
            x.xuat()
    def tinhTongLuong(self):
        if not self.dsNhanVien:
            print("Danh sach rong") 
            return
        print("Tong luong nhan vien la: {0}".format(sum(x.tinhLuong() for x in self.dsNhanVien)))            