from Actor import actor
from Film import film
from Customer import customer
import pandas as pd
class PythonAnalysis:

    # Xu ly actor table:

    def show_all(self, actor_list: list[actor]):
        data = []
        for x in actor_list:
            data.append([x.actor_id,x.first_name + " " + x.last_name,x.last_update])
        df = pd.DataFrame(data, columns=["ID","Name","Update Recently"])
        print("\n", df.to_string(index=False)) # Dùng cách này để loại bỏ chỉ số index 0,1,2,...
    def cout_actor(self, actor_list: list[actor]):
        print(f"So luong actor: {len(actor_list)}")
    def found_name_actor(self, actor_list: list[actor]):
        result = []
        canLoc = input("Nhap chu cai dau tien can tim trong first_name: ").upper()
        for x in actor_list:
            if x.first_name.startswith(canLoc):
                result.append(x)
        return result
    
    # Xu ly film table:

    def show_all_film(self, film_list: list[film]):
        data = []
        for x in film_list:
            data.append([x.film_id, x.title, x.description])
        df = pd.DataFrame(data, columns = ["Film_id","Title","Description"])
        print("\n", df.to_string(index=False))
    def sortBy_Id(self,film_list: list[film]):
        film_list.sort(key = lambda x : x.film_id, reverse = False)
        self.show_all_film(film_list)
    def found_film(self, film_list: list[film]):
        needFound = input("Nhap ten phim can tim: ").lower()
        checkExit = False
        for x in film_list:
            if needFound in x.title.lower():
                print(x)
                checkExit = True
        if checkExit == False:
            print("Khong tim thay")

    # Xy ly Customer table:
    def show_all_customer(self,customer_list: list[customer]):
        data = []
        for x in customer_list:
            data.append([x.customer_id, x.store_id, x.full_name(), x.email, x.address_id, x.activebool, x.create_date, x.last_update, x.active])
        df = pd.DataFrame(data, columns=["Customer_id","Store_id","Fullname","Email","Address_id","Activebool","Create_date","Last_update","Active"])
        print("\n",df.to_string(index=False))
    
            