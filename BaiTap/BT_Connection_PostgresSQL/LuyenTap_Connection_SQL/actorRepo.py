import pandas as pd
from Actor import actor
from DatabaseConnection import Database
class acTorRepo:
    def __init__(self,db: Database):
        self.db = db
    def fetch_all(self):
        query = "SELECT * FROM actor LIMIT 30"
        df = pd.read_sql(query, self.db.get_engine())
        actor_list = []
        for index, row in df.iterrows():
            Actor = actor(
                row["actor_id"],
                row["first_name"],
                row["last_name"],
                row["last_update"]
            )
            actor_list.append(Actor)
        return actor_list