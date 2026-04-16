class SimpleClass2: 
    # constructor
    def __init__(sefl):
        sefl.name = "Tung"
    # Methods
    def hello(sefl):
        print("Hello " + sefl.name)
    # Static methods
    @staticmethod
    def hi(name):
        print("Hi " + name)