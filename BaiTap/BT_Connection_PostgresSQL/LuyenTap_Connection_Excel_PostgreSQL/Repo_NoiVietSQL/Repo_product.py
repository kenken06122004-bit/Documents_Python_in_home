from Models_OBJ_data.Products import sanPham
from Database import db
import pandas as pd
class productsRepo:
    def __init__(self, database: db):
        self.database = database
    def fetch_all(self):
        query = """
        SELECT product_id, name, price, description
        FROM Products"""
        df = pd.read_sql(query, self.database.get_engine())
        list_product = []
        for index, row in df.iterrows():
            SP = sanPham(
                row["product_id"],
                row["name"],
                row["price"],
                row["description"]
            )
            list_product.append(SP)
        return list_product