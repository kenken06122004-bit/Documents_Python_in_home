from IFile import I_File
from KhachHang import khachHang
from Room import Phong
from PhongThuong import phongThuong
from PhongGiaDinh import phongGiaDinh
from PhongVip import phongVip
from NhanVien import nhanVien
import os
import pandas as pd
class QuanLyKhachSan(I_File):
    def __init__(self):
        self.dsPhong: list[Phong] = []
        self.dsKhachHang: list[khachHang] = []
        self.dsNhanVien: list[nhanVien] = []
    def docFile(self):
        #tenFile_phong = input("Nhap ten file can doc phong: ")
        tenFile_phong = "phong.txt"
        if not os.path.exists(tenFile_phong):
            print("File danh sach phong khong ton tai!")
            return
        #tenFile_khachHang = input("Nhap ten file can doc khach hang: ")
        tenFile_khachHang = "khachHang.txt"
        if not os.path.exists(tenFile_khachHang):
            print("File danh sach phong khong ton tai!")
            return
        #tenFile_nhanVien = input("Nhap ten file can doc nhan vien: ")
        tenFile_nhanVien = "nhanVien.txt"
        if not os.path.exists(tenFile_nhanVien):
            print("File danh sach phong khong ton tai!")
            return
        try:
            op = int(input("Ban muon doc file theo kieu gi: 1 = Doc theo cach binh thuong | 2 = Doc theo pandas ==> Lua chon: "))
        except Exception as e:
            print("Vui long nhap chu so --- Nhap lai")
            return
        else:
            if op == 1:
                self.docFile_Phong(tenFile_phong)
                self.docFile_khachHang(tenFile_khachHang)
                self.docFile_nhanVien(tenFile_nhanVien)
            elif op == 2:
                self.docFile_phong_pandas(tenFile_phong)
                self.docFile_khachHang_pandas(tenFile_khachHang)
                self.docFile_nhanVien_pandas(tenFile_nhanVien)
    def ghiFile(self):
        tenFile = input("Nhap ten file ban muon luu: ")
        op = int(input("Ban muon luu theo file loai nao: 1 = Phong | 2 = Khach hang | 3 = Nhan vien ==> "))
        if op == 1:
            self.ghiFile_phong(tenFile)
        elif op == 2:
            self.ghiFile_khachHang(tenFile)
        elif op == 3:
            self.ghiFile_nhanVien(tenFile)
        else:
            print("Chi nhap 1 --> 3")
    def docFile_Phong(self, tenFile):
        try:
            with open(tenFile,"r",encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line == "":
                        continue
                    mang = line.split(",")
                    if len(mang) == 4:
                        maPhong = mang[0].strip()
                        loaiPhong = mang[1].strip()
                        giaPhong = mang[2].strip()
                        trangThaiPhong = mang[3].strip()
                        if loaiPhong.lower().startswith("thuong"):
                            newPhong = phongThuong(maPhong,loaiPhong,giaPhong,trangThaiPhong)
                        elif loaiPhong.lower().startswith("family"):
                            newPhong = phongGiaDinh(maPhong,loaiPhong,giaPhong,trangThaiPhong)
                        elif loaiPhong.lower().startswith("vip"):
                            newPhong = phongVip(maPhong,loaiPhong,giaPhong,trangThaiPhong)
                        self.dsPhong.append(newPhong)
        except FileNotFoundError:
            print("Khong tim thay file")
        except Exception as e:
            print("Loi doc file: ", e)
        else:
            print("Doc thanh cong")
    def docFile_khachHang(self, tenFile):
        try:
            with open(tenFile,"r",encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line == "":
                        continue
                    mang = line.split(",")
                    if len(mang) == 4:
                        maKH = mang[0].strip()
                        tenKH = mang[1].strip()
                        sdt = mang[2].strip()
                        diaChi = mang[3].strip()
                        newKH = khachHang(maKH, tenKH, sdt, diaChi)
                        self.dsKhachHang.append(newKH)
        except FileNotFoundError:
            print("Khong tim thay file")
        except Exception as e:
            print("Loi doc file: ", e)
        else:
            print("Doc file thanh cong")
    def docFile_nhanVien(self, tenFile):
        try:
            with open(tenFile,"r",encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line == "":
                        continue
                    mang = line.split(",")
                    if len(mang) == 4:
                        maNV = mang[0].strip()
                        tenNV = mang[1].strip()
                        chucVu = mang[2].strip()
                        luong = mang[3].strip()
                        newNhanVien = nhanVien(maNV,tenNV,chucVu,luong)
                        self.dsNhanVien.append(newNhanVien)
        except FileNotFoundError:
            print("khong tim thay file")
        except Exception as e:
            print("Loi doc file: ", e)
        else: 
            print("Doc file thanh cong")
    def ghiFile_phong(self, tenFile):
        if not self.dsPhong:
            print("Danh sach rong. Khong the thuc hien")
            return
        else:
            try:
                duongDanFolderMuonLuu = input("Copy duong dan toi thu muc can lu (De trong de luu cung cap src): ")
                if duongDanFolderMuonLuu == "":
                    tenFileDayDu = tenFile
                else:
                    if not os.path.exists(duongDanFolderMuonLuu):
                        os.makedirs(duongDanFolderMuonLuu)
                        print(f"Da tao moi thu muc: {duongDanFolderMuonLuu}")
                    tenFileDayDu = os.path.join(duongDanFolderMuonLuu,tenFile)
                with open(tenFileDayDu,"w",encoding="utf-8") as f:
                    for x in self.dsPhong:
                        f.write(f"{x.ma}, {x.loai}, {x.gia}, {x.trangThai}\n")
            except Exception as e:
                print("Loi ghi file: ", e)
            else:
                print("Ghi file thanh cong")
    def ghiFile_khachHang(self, tenFile):
        if not self.dsKhachHang:
            print("Danh sach rong. Khong the thuc hien")
            return
        else:
            try:
                duongDanFolderMuonLuu = input("Copy duong dan toi thu muc can luu (De trong de luu cung cap src): ")
                if duongDanFolderMuonLuu == "":
                    tenFileDauDu = tenFile
                else:
                    if not os.path.exists(duongDanFolderMuonLuu):
                        os.makedirs(duongDanFolderMuonLuu)
                        print(f"Da tao moi thu muc: {duongDanFolderMuonLuu}")
                    tenFileDauDu = os.path.join(duongDanFolderMuonLuu,tenFile)
                with open(tenFileDauDu,"w",encoding="utf-8") as f:
                    for x in self.dsKhachHang:
                        f.write(f"{x.ma}, {x.ten}, {x.sdt}, {x.diaChi}\n")
            except Exception as e:
                print("Loi ghi file: ", e)
            else:
                print("Ghi file thanh cong")
    def ghiFile_nhanVien(self, tenFile):
        if not self.dsNhanVien:
            print("Danh sach rong. Khong the thuc hien")
            return
        else:
            try:
                duongDanFolderMuonLuu = input("Copy duong dan toi thu muc can luu (De trong de luu cung cap voi src): ")
                if duongDanFolderMuonLuu == "":
                    tenFileDayDu = tenFile
                else:
                    if not os.path.exists(duongDanFolderMuonLuu):
                        os.makedirs(duongDanFolderMuonLuu)
                        print(f"Da tao moi thu muc: {duongDanFolderMuonLuu}")
                    tenFileDayDu = os.path.join(duongDanFolderMuonLuu,tenFile)
                with open(tenFileDayDu,"w",encoding="utf-8") as f:
                    for x in self.dsNhanVien:
                        f.write(f"{x.ma}, {x.ten}, {x.chucVu}, {x.luong}\n")
            except Exception as e:
                print("Loi ghi file: ", e)
            else:
                print("Ghi file thanh cong")
    def bookPhong(self):
        maCanThue = input("Nhap ma phong can thue: ")
        maCanThue = maCanThue.upper()
        for x in self.dsPhong:
            if x.ma == maCanThue:
                if x.trangThai == "Trong":
                    print("Dat phong thanh cong")
                    x.trangThai = "Da thue"
                elif x.trangThai == "Da thue":
                    print("Phong da co nguoi thue")
                return
        print("Khong tim thay ma phong can thue")
    def checkOutRoom(self):
        maCanTra = input("Nhap ma phong can tra: ")
        maCanTra = maCanTra.upper()
        try:
            ngayThue = int(input("Nhap so ngay thue: "))
        except Exception as e:
            print("Ngay thue vui long nhap so")
        for x in self.dsPhong:
            if x.ma == maCanTra:
                if x.trangThai == "Da thue":
                    tienPhong = x.tinhTien(ngayThue)
                    x.trangThai = "Trong"
                    print("Tra phong thanh cong")
                    print("Tong tien: {0}".format(tienPhong))
                else:
                    print("Phong dang trong")
                return
            else:
                print("Khong tim thay phong")
    def hienThi(self):
        if not self.dsPhong and not self.dsKhachHang and not self.dsNhanVien:
            print("Danh sach rong. Khong the thuc hien")
            return
        else:
            while(True):
                op = int(input("Nhap; 0 = Thoat xem | 1 = Xem danh sach phong | 2 = Xem danh sach khach hang | 3 = Xem danh sach nhan vien ==> "))
                if op == 0: 
                    break
                elif op == 1:
                    for x in self.dsPhong:
                        x.hienThi()
                elif op == 2: 
                    for x in self.dsKhachHang:
                        x.hienThi()
                elif op == 3:
                    for x in self.dsNhanVien:
                        x.hienThi()
                else:
                    print("Chi nhap tu 0 --> 3")
# Pandas:
    def docFile_phong_pandas(self,tenFile):
        try:
            df = pd.read_csv(tenFile,sep=",",encoding="utf-8")
        except FileNotFoundError:
            print("Khong tim thay file")
        except Exception as e:
            print("Loi doc file: ",e)
        else:
            print("Doc file thanh cong")
            self.dsPhong.clear()
            for x in range(len(df)):
                maPhong = str(df.iloc[x,0].strip())
                loaiPhong = str(df.iloc[x,1].strip())
                giaPhong = int(df.iloc[x,2])
                trangThaiPhong = str(df.iloc[x,3].strip())
                if loaiPhong.lower().startswith("thuong"):
                    newPhong = phongThuong(maPhong,loaiPhong,giaPhong,trangThaiPhong)
                elif loaiPhong.lower().startswith("family"):
                    newPhong = phongGiaDinh(maPhong,loaiPhong,giaPhong,trangThaiPhong)
                elif loaiPhong.lower().startswith("vip"):
                    newPhong = phongVip(maPhong,loaiPhong,giaPhong,trangThaiPhong)
                self.dsPhong.append(newPhong)
    def docFile_khachHang_pandas(self,tenFile):
        try:
            df = pd.read_csv(tenFile,sep=",",encoding="utf-8")
        except FileNotFoundError:
            print("Khong tim thay file")
        except Exception as e:
            print("Loi doc file: ",e)
        else:
            print("Doc file thanh cong")
            self.dsKhachHang.clear()
            for x in range(len(df)):
                maKhachHang = str(df.iloc[x,0].strip())
                tenKhachHang = str(df.iloc[x,1].strip())
                sdtKhachHang = str(df.iloc[x,2])
                diaChiKhachHang = str(df.iloc[x,3].strip())
                self.dsKhachHang.append(khachHang(maKhachHang,tenKhachHang,sdtKhachHang,diaChiKhachHang))
    def docFile_nhanVien_pandas(self,tenFile):
        try:
            df = pd.read_csv(tenFile,sep=",",encoding="utf-8")
        except FileNotFoundError:
            print("Khong tim thay file")
        except Exception as e:
            print("Loi doc file: ",e)
        else:
            print("Doc file thanh cong")
            self.dsNhanVien.clear()
            for x in range(len(df)):
                maNhanVien = str(df.iloc[x,0].strip())
                tenNhanVien = str(df.iloc[x,1].strip())
                chucVuNhanVien = str(df.iloc[x,2].strip())
                luongNhanVien = int(df.iloc[x,3])
                self.dsNhanVien.append(nhanVien(maNhanVien,tenNhanVien,chucVuNhanVien,luongNhanVien))
    def xuat_pandas_phong(self):
        if not self.dsPhong:
            print("Danh sach rong. Khong the thuc hien")
            return
        else:
            data = []
            for x in self.dsPhong:
                data.append([x.ma,x.loai,x.gia,x.trangThai])
            df = pd.DataFrame(data, columns=["Ma phong","Loai phong","Gia phong","Trang thai"])
            print("========== DANH SACH PHONG ==========")
            print(df)
    def xuat_pandas_khachHang(self):
        if not self.dsKhachHang:
            print("Danh sach rong. Khong the thuc hien")
            return
        else:
            data = []
            for x in self.dsKhachHang:
                data.append([x.ma,x.ten,x.sdt,x.diaChi])
            df = pd.DataFrame(data, columns=["Ma khach hang","Ten khach hang","So dien thoai","Dia chi"])
            print("========== DANH SACH KHACH HANG ==========")
            print(df)      
    def xuat_pandas_nhanVien(self):
        if not self.dsNhanVien:
            print("Danh sach rong. Khong the thuc hien")
            return
        else:
            data = []
            for x in self.dsNhanVien:
                data.append([x.ma,x.ten,x.chucVu,x.luong])
            df = pd.DataFrame(data, columns=["Ma nhan vien","Ten nhan vien","Chuc vu","So dien thoai"])
            print("========== DANH SACH NHAN VIEN ==========")
            print(df)    
    def hienThi_pandas(self):
        if not self.dsPhong and not self.dsKhachHang and not self.dsNhanVien:
            print("Danh sach rong. Khong the thuc hien")
            return
        else:
            while(True):
                try:
                    op = int(input("Nhap: 0 = Thoat | 1 = Xem danh sach phong | 2 = Xem danh sach khach hang | 3 = Xem danh sach nhan vien ==> "))
                except Exception as e:
                    print("Loi: ",e)
                else:
                    if op == 0:
                        break
                    elif op == 1:
                        self.xuat_pandas_phong()
                    elif op == 2:
                        self.xuat_pandas_khachHang()
                    elif op == 3:
                        self.xuat_pandas_nhanVien()
                    else:
                        print("Chi nhap 0 --> 3")
            