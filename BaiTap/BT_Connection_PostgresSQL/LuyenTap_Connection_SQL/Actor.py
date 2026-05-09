class actor:
    def __init__(self, actor_id = "", first_name = "", last_name = "", last_update = ""):
        self.actor_id = actor_id
        self.first_name = first_name
        self.last_name = last_name
        self.last_update = last_update
    def full_name(self):
        return self.first_name + " " + self.last_name
    def __str__(self):
        return f"ID: {self.actor_id} | Name: {self.full_name()} | Update recently: {self.last_update}"        