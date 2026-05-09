class customer:
    def __init__(self, customer_id = 0, store_id = 0, first_name = "", last_name = "", email = "", address_id = 0, activebool = False, create_date = "", last_update = "", active = 0):
        self.customer_id = customer_id
        self.store_id = store_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address_id = address_id
        self.activebool = activebool
        self.create_date = create_date
        self.last_update = last_update
        self.active = active
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return f"Customer_id: {self.customer_id} | Store_id: {self.store_id} | Fullname: {self.full_name()} | Email: {self.email} | Address: {self.address_id} | Activebool: {self.activebool} | Create_date: {self.create_date} | Active: {self.active}"