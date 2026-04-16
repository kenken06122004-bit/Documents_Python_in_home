from SinhVien import SV
class DanhSachSV:
    def __init__(self):
        self.ds: list[SV] = []
    def themSV(self):
        sv = SV()
        sv.themThongTin()
        self.ds.append(sv)
    def xuatDS(self):
        print("====== DANH SACH SINH VIEN ======")
        for x in self.ds:
            x.xuatThongTin()
    def timSV_gioiNhat(self):
        if not self.ds:
            print("Danh sach rong")
            return None
        else:
            sv_gioi = max(self.ds,key=lambda x: x.tinhDiemTB())
    def sapXepTheoDiemTB(self):
        self.ds.sort(key=lambda x : x.tinhDiemTB(),reverse=True)
