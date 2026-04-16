"""
Bài tập: 
    Xây dựng class Ngay, thuộc tính gồm có: ngày, tháng, năm
    Xây dựng các methods:
        + Cho biết đó là ngày thứ bao nhiêu trong năm
        + Static methods: cho biết thang đó có bao nhiêu ngày
"""
from Ngay import Ngay
ngayA = Ngay(15,3,2022)
print(ngayA.ngayTrongNam())