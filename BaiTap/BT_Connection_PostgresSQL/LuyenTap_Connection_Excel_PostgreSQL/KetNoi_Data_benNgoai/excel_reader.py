import pandas as pd
class ExcelReader:
    def read_excel(self, path):
        customer_df = pd.read_excel(path, sheet_name="Customer")
        product_df = pd.read_excel(path, sheet_name="Products")
        order_df = pd.read_excel(path, sheet_name="Order")
        return customer_df, product_df, order_df