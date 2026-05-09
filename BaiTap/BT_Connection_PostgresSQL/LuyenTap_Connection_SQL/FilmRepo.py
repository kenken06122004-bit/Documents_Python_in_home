import pandas as pd
from Film import film
from DatabaseConnection import Database
class filmRepo:
    def __init__(self, db: Database):
        self.db = db
    def fetch_all(self):
        query = """SELECT * FROM film LIMIT 30"""
        df = pd.read_sql(query, self.db.get_engine())
        film_list = []
        for index, row in df.iterrows():
            Film = film(row["film_id"], row["title"], row["description"])
            film_list.append(Film)
        return film_list