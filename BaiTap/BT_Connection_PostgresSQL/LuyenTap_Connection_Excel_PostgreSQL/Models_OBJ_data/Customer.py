class KhachHang:
    def __init__(self, customer_id = 0, name = "", email = "", address = ""):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.address = address
    def __str__(self):
        return f"{self.customer_id} | {self.name} | {self.email} | {self.address}"