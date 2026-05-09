class sanPham:
    def __init__(self, product_id = 0, name = "", price = 0.0, description = ""):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.description = description
    def __str__(self):
        return f"{self.product_id} | {self.name} | {self.price}"