from DatabaseConnection import Database
from actorRepo import acTorRepo
from FilmRepo import filmRepo
from CustomerRepo import customerRepo
from PythonAnalysis import PythonAnalysis
def main():
    # Ket noi Database

    db = Database()

    # Kết nối các kiểu dữ liệu của các đối tượng:

    Actorrepo = acTorRepo(db)
    Filmrepo = filmRepo(db)
    CustomerRepo = customerRepo(db)

    # Kết nối với class xử lý dữ liệu:

    analysis = PythonAnalysis()

    # Methods in Actor:
    try:
        option = int(input("Menu: 1 = Actor | 2 = Film | 3 = Customer  ==> Your select: "))
    except Exception as e:
        print("Loi: ", e)
    if option == 1:
        try:
            actor_list = Actorrepo.fetch_all()
            print("========== DANH SACH ACTOR ==========")
            analysis.show_all(actor_list)
            print("========== SO LUONG ==========")
            analysis.cout_actor(actor_list)
            print("========== LOC THEO TEN ==========")
            result = analysis.found_name_actor(actor_list)
            for x in result:
                print(x)
        except Exception as e:
            print("Loi: ", e)
    
    # Methods in Film:
    elif option == 2:
        try:
            film_list = Filmrepo.fetch_all()
            print("========== DANH SACH PHIM ==========")
            analysis.show_all_film(film_list)
            print("========== DANH SACH PHIM SAU KHI SAP XEP ==========")
            analysis.sortBy_Id(film_list)
            print("========== TIM PHIM ==========")
            analysis.found_film(film_list)
        except Exception as e:
            print("Loi: ", e)
    
    # Methods in Customer:
    elif option == 3:
        try:
            customer_list = CustomerRepo.fetch_all()
            print("========== DANH SACH KHACH HANG ==========")
            analysis.show_all_customer(customer_list)
        except Exception as e:
            print("Loi: ", e)
if __name__ == "__main__":
    main()