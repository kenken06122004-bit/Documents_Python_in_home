import psycopg2

try:
    conn = psycopg2.connect(
        host="127.0.0.1",
        port="5432",
        user="postgres",
        password="Nguyenvanphi2004@",
        database="SQL_learn_in_home"
    )

    print("Ket noi thanh cong")

except Exception as e:
    print("Loi:", e)