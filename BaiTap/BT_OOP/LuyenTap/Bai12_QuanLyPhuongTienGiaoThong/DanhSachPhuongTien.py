from PhuongTien import PhuongTien
from Oto import Oto
from XeMay import xeMay
from XeTai import xeTai
class DanhSachPT:
    def __init__(self):
        self.ds: list[PhuongTien] = []
    def docFile(self):
        try:
            with open("D:\\Python_in_VScode\\BaiTap\\BT_OOP\\LuyenTap\\Bai12_QuanLyPhuongTienGiaoThong\\docFile.txt","r",encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line == "":
                        continue
                    arr = line.split(",")
                    if len(arr) == 6:
                        loaiPT = arr[0].lower()
                        maPT = arr[1]
                        hangSX = arr[2]
                        gia = int(arr[3])
                        namSX = int(arr[4])
                        if loaiPT.startswith("oto"):
                            soCho = int(arr[5])
                            newPT = Oto(maPT,hangSX,gia,namSX,soCho)
                            self.ds.append(newPT)
                        elif loaiPT.startswith("xemay"):
                            congSuat = int(arr[5])
                            newPT = xeMay(maPT,hangSX,gia,namSX,congSuat)
                            self.ds.append(newPT)
                        elif loaiPT.startswith("xetai"):
                            trongTai = int(arr[5])
                            newPT = xeTai(maPT,hangSX,gia,namSX,trongTai)
                            self.ds.append(newPT)
                    else:
                        print("File qua ky tu")
        except Exception as e:
            print("Loi doc file: ",e)
        else:
            print("Doc file thanh cong")
    def xuat(self):
        if not self.ds:
            print("Danh sach rong")
            return
        print("====== DANH SACH PHUONG TIEN ======")
        for x in self.ds:
            x.xuat()