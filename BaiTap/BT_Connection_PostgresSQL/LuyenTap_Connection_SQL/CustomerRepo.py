from Customer import customer
from DatabaseConnection import Database
import pandas as pd
class customerRepo:
    def __init__(self, db: Database):
        self.db = db
    def fetch_all(self):
        query = "SELECT * FROM customer LIMIT 30"
        df = pd.read_sql(query, self.db.get_engine())
        customer_list = []
        for index, row in df.iterrows():
            KH = customer(row["customer_id"],row["store_id"],row["first_name"],row["last_name"],row["email"],row["address_id"],row["activebool"],row["create_date"],row["last_update"],row["active"])
            customer_list.append(KH)
        return customer_list