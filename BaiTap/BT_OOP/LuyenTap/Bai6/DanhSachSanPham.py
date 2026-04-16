from SanPham import SP
class DanhSachSP():
    def __init__(self):
        self.ds: list[SP] = [] 
    def them(self):
        sp = SP()
        sp.nhap()
        self.ds.append(sp)
    def tongTien(self):
        tong = 0
        for x in self.ds:
            tong += x.thanhTien()
        return tong
    def timGiaCaoNhat(self):
        if not self.ds: # Neu danh sach rong
            return None
        return max(self.ds,key=lambda x: x.giaBan)
    def xuatDanhSach(self):
        print("====== DANH SACH SAN PHAM ======")
        for x in self.ds:
            x.xuat()
        print("Tong tien: {0}".format(self.tongTien()))