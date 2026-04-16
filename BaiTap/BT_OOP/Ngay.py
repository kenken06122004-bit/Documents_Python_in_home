class Ngay:
    # Constructor:
    def __init__(self, giaTri_Ngay, giaTri_Thang, giaTri_Nam):
        self.ngay = giaTri_Ngay
        self.thang = giaTri_Thang
        self.nam = giaTri_Nam
    # Xác định số ngày của tháng:
    @staticmethod
    def soNgayCuaThang(thang, nam):
        if thang in [1,3,5,7,8,10,12] :
            return 31
        elif thang in [4,6,9,11] :
            return 30
        elif thang == 2:
            if nam % 400 == 0 or nam % 4 == 0 and nam % 100 != 0:
                return 29
            else:
                return 28
    def ngayTrongNam(self):
        giaTriNgayTrongNam = 0
        # Tính tổng số lượng ngày của những tháng trước
        for x in range(1,self.thang):
            giaTriNgayTrongNam += self.soNgayCuaThang(x, self.nam)
        # Cộng thêm số ngày của tháng hiện tại
        giaTriNgayTrongNam += self.ngay
        # Trả về kết quả
        return giaTriNgayTrongNam


        