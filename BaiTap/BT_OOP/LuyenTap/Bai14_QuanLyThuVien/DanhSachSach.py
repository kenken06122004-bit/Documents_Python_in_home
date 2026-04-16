from Sach import Sach
from SachGiaoKhoa import SachGK
from SachThamKhao import SachTK
import os
import pandas as pd
class DanhSachSach:
    def __init__(self):
        self.ds: list[Sach] = []
# Cách đọc - ghi - xuất file theo cách thông thường:
    def xuatForDocFileThuong(self):
        if not self.ds:
            print("Danh sach rong. Khong the thuc hien !")
            return
        print("========= DANH SACH SACH =========")
        for x in self.ds:
            x.hienThi()
    def docFile(self,tenFile):
        try:
            with open(tenFile,"r",encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line == "":
                        continue
                    mang = line.split(",")
                    if len(mang) == 5:
                        maSach = mang[0].strip()
                        tenSach = mang[1].strip()
                        tenTacGia = mang[2].strip()
                        giaBan = int(mang[3].strip())
                        if maSach.startswith("SGK"):
                            tinhTrang = mang[4].strip().lower() == "true" # Ở đây chúng ta sẽ phải so sánh chuỗi chứ nếu dùng bool sẽ không chạy đúng
                            newSach = SachGK(maSach,tenSach,tenTacGia,giaBan,tinhTrang)
                        elif maSach.startswith("STK"):
                            thue = float(mang[4].strip())
                            newSach = SachTK(maSach,tenSach,tenTacGia,giaBan,thue)
                        self.ds.append(newSach)
        except FileNotFoundError:
            print("Khong tim thay file")
        except Exception as e:
            print("Loi doc file: ",e)
        else:
            print("Doc file thanh cong")
    def ghiFile(self, tenFile):
        if not self.ds:
            print("Danh sach rong. Khong the thuc hien !")
            return
        try:
            duongDanFolderMuonLuu = input("Copy duong dan toi thu muc can luu (De trong neu muon luu cung cap thu muc): ")
            if duongDanFolderMuonLuu == "":
                tenFileDayDu = tenFile
            else:
                if not os.path.exists(duongDanFolderMuonLuu):
                    os.makedirs(duongDanFolderMuonLuu)
                    print(f"Da tao moi thu muc: {duongDanFolderMuonLuu}")
                tenFileDayDu = os.path.join(duongDanFolderMuonLuu,tenFile)
            with open(tenFileDayDu,"w",encoding="utf-8") as f:
                for x in self.ds:
                    if isinstance(x,SachGK):
                        f.write(f"{x.maSach}, {x.tenSach}, {x.tacGia}, {x.gia}, {x.tinhTrang}\n")
                    elif isinstance(x,SachTK):
                        f.write(f"{x.maSach}, {x.tenSach}, {x.tacGia}, {x.gia}, {x.thue}\n")
        except Exception as e:
            print("Loi ghi file: ", e)
        else:
            print("Ghi file thanh cong")
# Cách đọc - ghi - xuất file theo cách pandas:
    def docFile_pandas(self,tenFile):
        try:
            df = pd.read_csv(tenFile,sep=",",encoding="utf-8")
        except FileNotFoundError:
            print("Khong tim thay file")
        except Exception as e:
            print("Loi doc file: ", e)
        else:
            print("Doc file thanh cong")
        self.ds.clear()
        for x in range(len(df)):
            maSach = df.iloc[x,0].strip()
            tenSach = df.iloc[x,1].strip()
            tenTacGia = df.iloc[x,2].strip()
            giaBan = int(df.iloc[x,3])
            if maSach.startswith("SGK"):
                tinhTrang = bool(df.iloc[x,4])
                newSach = SachGK(maSach,tenSach,tenTacGia,giaBan,tinhTrang)
            elif maSach.startswith("STK"):
                thue = float(df.iloc[x,4])
                newSach = SachTK(maSach,tenSach,tenTacGia,giaBan,thue)
            self.ds.append(newSach)