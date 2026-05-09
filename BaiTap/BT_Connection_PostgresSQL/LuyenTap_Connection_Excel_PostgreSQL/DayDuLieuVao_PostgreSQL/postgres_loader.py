from Database import db
import pandas as pd
class PostgreLoader:
    def __init__(self, db: db):
        self.db = db
    def load_customer(self, customer_df: pd.DataFrame):
        customer_df.to_sql(
            name="customer",
            con=self.db.get_engine(),
            if_exists="replace",
            index=False
        )
        print("Da load customer")
    def load_product(self, product_df: pd.DataFrame):
        product_df.to_sql(
            name="products",
            con=self.db.get_engine(),
            if_exists="replace",
            index=False
        )
        print("Da load products")
    def load_order(self, order_df: pd.DataFrame):
        order_df.to_sql(
            name="oder",
            con=self.db.get_engine(),
            if_exists="replace",
            index=False
        )
        print("Da load order")