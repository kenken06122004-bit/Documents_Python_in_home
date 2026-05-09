class od:
    def __init__(self, order_id = 0, customer_id = 0, product_id = 0, order_date = ""):
        self.order_id = order_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.order_date = order_date
    def __str__(self):
        return f"{self.order_id} | {self.customer_id} | {self.product_id} | {self.order_date}"
