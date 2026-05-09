from Database import db
import pandas as pd
from Models_OBJ_data.Order import od
class orderRepo:
    def __init__(self, database: db):
        self.database = database
    def fetch_all(self):
        query = """SELECT order_id, customer_id, product_id, order_date
        FROM Order"""
        df = pd.read_sql(query, self.database.get_engine())
        list_order = []
        for index, row in df.iterrows():
            obj_od = od(
                row["order_id"],
                row["customer_id"],
                row["product_id"],
                row["order_date"]
            )
            list_order.append(obj_od)
        return list_order