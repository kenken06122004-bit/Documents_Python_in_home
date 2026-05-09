from sqlalchemy import create_engine
from sqlalchemy.engine import URL
class Database:
    def __init__(self):
        url = URL.create(
            drivername="postgresql+psycopg2",
            username="postgres",
            password="Nguyenvanphi2004@",
            host="127.0.0.1",
            port=5432,
            database="SQL_learn_in_home"
        )
        self.engine = create_engine(url)
    def get_engine(self):
        return self.engine