from Database import db
import pandas as pd
from Models_OBJ_data.Customer import KhachHang
class repoCustomer:
    def __init__(self, db: db):
        self.db = db
    def fetch_all(self):
        query = """
        SELECT customer_id, name, email, address
        FROM Customer"""
        df = pd.read_sql(query, self.db.get_engine())
        list_customer = []
        for index, row in df.iterrows():
            KH = KhachHang(
                row["customer_id"],
                row["name"],
                row["email"],
                row["address"]
            )
            list_customer.append(KH)
        return list_customer