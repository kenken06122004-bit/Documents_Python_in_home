from MonAn import MonAn
from MonChinh import monChinh
from TrangMieng import trangMieng
from DoUong import doUong
import os
import pandas as pd
class danhSach:
    def __init__(self):
        self.ds: list[MonAn] = []
# Không dùng pandas:
    def readF(self,tenFile):
        self.ds.clear()
        try:
            with open(tenFile,"r",encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line == "":
                        continue
                    else:
                        a = line.split(",")
                        if len(a) == 4:
                            maMon = a[0].strip()
                            tenMon = a[1].strip()
                            gia = int(a[2].strip())
                            thuocTinhCuoi = a[3].strip()
                            if maMon.startswith("MC"):
                                newMonAn = monChinh(maMon,tenMon,gia,thuocTinhCuoi)
                            elif maMon.startswith("TM"):
                                newMonAn = trangMieng(maMon,tenMon,gia,int(thuocTinhCuoi))
                            elif maMon.startswith("DU"):
                                newMonAn = doUong(maMon,tenMon,gia,thuocTinhCuoi.lower() == "true")
                            else:
                                continue
                            self.ds.append(newMonAn)
        except FileNotFoundError:
            print("Không tìm thấy file")
        except Exception as e:
            print("Lỗi: ", e)
        else:
            print("Thanh cong")
    def writeF(self,tenFile):
        if not self.ds:
            print("Rỗng --> Không thể thực hiện")
            return
        else:
            try:
                linkFolderSave = input("Copy đường dẫn tới thư mục muốn lưu (Để trống nếu muốn lưu cùng cấp với src): ")
                if linkFolderSave == "":
                    nameFileFull = tenFile
                else:
                    if not os.path.exists(linkFolderSave):
                        os.makedirs(linkFolderSave)
                        print("Thư mục chưa tồn tại --> Đã tạo mới thư mục")
                    nameFileFull = os.path.join(linkFolderSave,tenFile)
                with open(nameFileFull,"w",encoding="utf-8") as f:
                    for x in self.ds:
                        if isinstance(x,monChinh):
                            f.write(f"{x.maMon}, {x.tenMon}, {x.gia}, {x.size}\n")
                        elif isinstance(x,trangMieng):
                            f.write(f"{x.maMon}, {x.tenMon}, {x.gia}, {x.giamGia}\n")
                        elif isinstance(x,doUong):
                            f.write(f"{x.maMon}, {x.tenMon}, {x.gia}, {x.coDa}\n")
            except Exception as e:
                print("Loi: ",e)
            else:
                print("Thanh cong")
# Dùng pandas:
    def readFPandas(self,tenFile):
        try:
            df = pd.read_csv(tenFile,sep=",",encoding="utf-8")
        except FileNotFoundError:
            print("Khong tim thay")
            return
        except Exception as e:
            print("Loi: ",e)
            return
        else:
            print("Thanh cong")
        self.ds.clear()
        for x in range(len(df)):
            maMon = df.iloc[x,0].strip()
            tenMon = df.iloc[x,1].strip()
            gia = int(df.iloc[x,2])
            thuocTinhCuoi = df.iloc[x,3].strip()
            if maMon.startswith("MC"):
                newMonAn = monChinh(maMon,tenMon,gia,thuocTinhCuoi)
            elif maMon.startswith("TM"):
                newMonAn = trangMieng(maMon,tenMon,gia,int(thuocTinhCuoi))
            elif maMon.startswith("DU"):
                newMonAn = doUong(maMon,tenMon,gia,thuocTinhCuoi.lower() == "true")
            self.ds.append(newMonAn)
# Các chức năng khác: 
    def addMon(self):
        while(True):
            print("Bạn muốn thêm vào menu món nào: 1 = Món chính | 2 = Tráng miệng | 3 = Đồ uống")
            op = int(input("Nhập lựa chọn: "))
            print("========= THÔNG TIN MÓN =========")
            maMon = input("Mã món: ")
            tenMon = input("Tên món: ")
            gia = int(input("Giá bán: "))
            match(op):
                case 0:
                    break
                case 1:
                    cuoi = input("Size: ")
                case 2:
                    cuoi = int(input("Giam gia: "))
                case 3: 
                    cuoi = input("Ice(True/False): ")
            newMon = monChinh(maMon,tenMon,gia,cuoi)
            self.ds.append(newMon)
            print("Them thanh cong")
        