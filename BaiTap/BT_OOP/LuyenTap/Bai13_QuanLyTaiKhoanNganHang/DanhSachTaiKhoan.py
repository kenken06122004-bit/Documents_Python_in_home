from TaiKhoan import TaiKhoan
from TaiKhoanTietKiem import taiKhoanTietKiem
from TaiKhoanVangLai import taiKhoanVangLai
import os
import pandas as pd
class danhSachTK:
    def __init__(self):
        self.ds: list[TaiKhoan] = []
    def docFile(self,tenFile):
        try:
            with open(tenFile,"r",encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line == "":
                        continue
                    arr = line.split(",")
                    if len(arr) == 5:
                        loaiTK = arr[0].strip()
                        soTK = arr[1].strip()
                        tenChuTK = arr[2].strip()
                        soDu = int(arr[3].strip())
                        if loaiTK == "TaiKhoanTietKiem":
                            laiSuat = float(arr[4].strip())
                            newTK = taiKhoanTietKiem(soTK,tenChuTK,soDu,laiSuat)
                        elif loaiTK == "TaiKhoanVangLai":
                            phiDuyTri = int(arr[4].strip())
                            newTK = taiKhoanVangLai(soTK,tenChuTK,soDu,phiDuyTri)
                        self.ds.append(newTK)
        except FileNotFoundError:
            print("Khong tim thay file")
        except Exception as e:
            print("Loi doc file: ", e)
        else:
            print("Doc file thanh cong")
    def ghiFile(self, tenFile):
        if not self.ds:
            print("Danh sach rong")
            return
        try:
            duongDanFolderMuonLuu = input("Copy duong dan toi thu muc muon luu file (bo trong de luu cung cap thu muc): ")
            if duongDanFolderMuonLuu == "":
                tenFileDayDu = tenFile
            else:
                if not os.path.exists(duongDanFolderMuonLuu): # Kiểm tra xem thư mục đã tồn tại hay chưa, nếu chưa thì tạo mới
                    os.makedirs(duongDanFolderMuonLuu)
                    print(f"Da tao moi thu muc: {duongDanFolderMuonLuu}")
                tenFileDayDu = os.path.join(duongDanFolderMuonLuu,tenFile) # Nối tên file an toàn
            with open(tenFileDayDu,"w",encoding="utf-8") as f:
                for x in self.ds:
                    if isinstance(x,taiKhoanTietKiem):
                        f.write(f"{x.soTK}, {x.tenChuTK}, {x.soDu}, {x.laiSuat}\n")
                    elif isinstance(x,taiKhoanVangLai):
                        f.write(f"{x.soTK}, {x.tenChuTK}, {x.soDu}, {x.phiDuyTri}\n")
        except Exception as e:
            print("Loi ghi file: ",e)
        else:
            print("Ghi file thanh cong") 
# Lưu ý: Khai báo thư viện os trước khi dùng
    def docFile_bang_Pandas(self,tenFile):
        try:
            df = pd.read_csv(tenFile,sep=",",encoding="utf-8") 
        except FileNotFoundError:
            print("Khong tim thay file")
        except Exception as e:
            print("Loi doc file: ",e)
        else:
            print("Doc file thanh cong")
        # Xoa danh sach cu (Neu co):
        self.ds.clear()
        # Duyet tung dong du lieu trong bang:
        for i in range(len(df)):
            loai = df.iloc[i,0].strip()
            soTK = df.iloc[i,1].strip()
            tenChuTK = df.iloc[i,2].strip()
            soDu = int(df.iloc[i,3])
            truongCuoi = float(df.iloc[i,4])
            if loai == "TaiKhoanTietKiem":
                newTK = taiKhoanTietKiem(soTK,tenChuTK,soDu,truongCuoi)
            elif loai == "TaiKhoanVangLai":
                newTK = taiKhoanVangLai(soTK,tenChuTK,soDu,truongCuoi)
            self.ds.append(newTK)
# Đọc file xong thì nó sẽ không lưu về ds đã tạo ban đầu nên phải code thêm dòng dưới để lưu về ds ban đầu
# Lưu ý: ở đây khác với đọc file thường là: df.iloc[i,3] không phải kiểu string nên không dùng được strip()
# vì khi chúng ta đọc file bằng pandas thì pandas sẽ tự hiểu được kiểu dữ liệu của thuộc tính đó, nên chúng ta ép kiểu dữ liệu cũng được không ép cũng được
    def ghiFile_bang_Pandas(self, tenFile):
        if not self.ds:
            print("Danh sach rong")
            return
        try:
            duongDanFolderMuonLuu = input("Copy duong dan toi thu muc muon luu (bo trong neu muon luu file cung cap thu muc): ")
            if duongDanFolderMuonLuu == "":
                tenFileDayDu = tenFile
            else:
                if not os.path.exists(duongDanFolderMuonLuu):
                    os.makedirs(duongDanFolderMuonLuu)
                    print(f"Da tao moi thu muc: {duongDanFolderMuonLuu}")
                tenFileDayDu = os.path.join(duongDanFolderMuonLuu, tenFile)
            data = []
            for x in self.ds:
                if isinstance(x,taiKhoanTietKiem):
                    data.append(["TaiKhoanTietKiem", x.soTK, x.tenChuTK, x.soDu, x.laiSuat])
                elif isinstance(x,taiKhoanVangLai):
                    data.append(["TaiKhoanVangLai", x.soTK, x.tenChuTK, x.soDu, x.phiDuyTri])
            df = pd.DataFrame(data, columns=["Loai tai khoan","So tai khoan","Ten nguoi so huu","So du kha dung","Lai suat_Phi duy tri"])
            df.to_csv(tenFileDayDu,index=False,encoding="utf-8")
        except Exception as e:
            print("Loi ghi file: ", e)
        else:
            print("Ghi file thanh cong")
# Chú ý: ds = list (Tức là danh sách chứa các đối tượng tùy chỉnh && self.ds = [obj1, obj2, .....]) nên pandas sẽ không biết lấy thuộc tính nào làm cột ==> không tạo bảng được
# Chính vì thế chúng ta sẽ tạo list rỗng data để đưa các đối tượng trong self.ds về kiểu dữ liệu list để pandas có thể hiểu được
    def xuat(self):
        if not self.ds:
            print("Danh sach rong")
            return
        data = []
        for x in self.ds:
            if isinstance(x,taiKhoanTietKiem):
                    data.append(["TaiKhoanTietKiem", x.soTK, x.tenChuTK, x.soDu, x.laiSuat])
            elif isinstance(x,taiKhoanVangLai):
                    data.append(["TaiKhoanVangLai", x.soTK, x.tenChuTK, x.soDu, x.phiDuyTri])
        df = pd.DataFrame(data, columns=["Loai tai khoan","So tai khoan","Ten nguoi so huu","So du kha dung","Lai suat_Phi duy tri"])
        print("========= DANH SACH TAI KHOAN =========")
        print(df)