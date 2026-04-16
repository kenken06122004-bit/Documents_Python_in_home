from NhanVien import NV
from NhanVien_HanhChinh import HanhChinh
from NhanVien_KinhDoanh import KinhDoanh
class danhSach:
    def __init__(self):
        self.ds: list[NV] = []
    def themNV(self):
#        nv = NV() # Khong the tao doi tuong vi la lop truu tuong
#        nv.nhap()
#        self.ds.append(nv)
        while True:
            print("Chon: 0 = Thoat | 1 = Them nhan vien hanh chinh | 2 = Them nhan vien kinh doanh\n")
            op = int(input("Nhap lua chon: "))
            if op == 0: 
                break
            elif op == 1:
                nv = HanhChinh()
                nv.nhap()
                self.ds.append(nv)
            elif op == 2:
                nv = KinhDoanh()
                nv.nhap()
                self.ds.append(nv)
            else:
                print("Chi nhap 0 | 1 | 2")
    def xuatNV(self):
        print("====== DANH SACH NHAN VIEN ======\n")
        for x in self.ds:
            x.xuat()
    def tinhTongLuong(self):
        tong = 0
        for x in self.ds:
            tong = tong + x.tinhLuong()
        print(f"Tong luong nhan vien: {tong}")
    def sapXepTheoLuong(self):
        self.ds.sort(key=lambda x : x.tinhLuong(),reverse=True)  
        print("\nDanh sach nhan vien sau khi sap xep giam dan la:\n")
        self.xuatNV()
    def demSoNhanVienTungLoai(self):
        demHanhChinh = 0
        demKinhDoanh = 0
        for x in self.ds:
            if isinstance(x,HanhChinh):
                demHanhChinh += 1
            elif isinstance(x,KinhDoanh):
                demKinhDoanh += 1
        print(f"\nSo nhan vien Hanh Chinh la: {demHanhChinh}")
        print(f"So nhan vien Kinh Doanh la: {demKinhDoanh}")