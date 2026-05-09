from Services.analysis_service import ANA_ser
from DayDuLieuVao_PostgreSQL.postgres_loader import PostgreLoader
from KetNoi_Data_benNgoai.excel_reader import ExcelReader
from Repo_NoiVietSQL.Repo_customer import repoCustomer
from Repo_NoiVietSQL.Repo_product import productsRepo
from Repo_NoiVietSQL.Repo_order import orderRepo
from Database import db
def main():
    # Connection DATABASE:
    database = db()

    # Connection EXCEL:
    reader = ExcelReader()
    customer_df, product_df, order_df = reader.read_excel("C:\\Users\\ADMIN\\Downloads\\Bảng tính không có tiêu đề.xlsx")

    # Load data from EXCEL to SQL:
    pushDf = PostgreLoader(database)
    pushDf.load_customer(customer_df)
    pushDf.load_product(product_df)
    pushDf.load_order(order_df)

    # Connection REPO of DATA:
    repo_customer = repoCustomer(database)
    repo_product = productsRepo(database)
    repo_order = orderRepo(database)

    # Connection analysis class:
    ana_data = ANA_ser()

    # Methods:
    try:
        option = int(input("SELECT: 1 = Ana_Customer | 2 = Ana_Product | 3 = Ana_Order ==> Your choose: "))
        if option == 1:
            list_customer = repo_customer.fetch_all()
            print("=" * 10 + " LIST CUSTOMER " + "=" * 10)
            ana_data.show_all(list_customer)
    except Exception as e:
        print("Error: ", e) 
if __name__ == "__main__":
    main()