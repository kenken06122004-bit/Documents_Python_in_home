class film:
    def __init__(self, film_id = 0, title = "", description = ""):
        self.film_id = film_id
        self.title = title
        self.description = description
    def __str__(self):
        return f"Film_ID: {self.film_id} | Title: {self.title} | Description: {self.description}"