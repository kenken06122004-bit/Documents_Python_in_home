from Models_OBJ_data.Customer import KhachHang
from Models_OBJ_data.Products import sanPham
from Models_OBJ_data.Order import od
import pandas as pd
class ANA_ser:
    def show_all_customer(self, list_customer: list[KhachHang]):
        data = []
        for x in list_customer:
            data.append([x.customer_id, x.name, x.email, x.address])
        df = pd.DataFrame(data, columns=["Customer_id","Name","Email","Address"])
        print(df)