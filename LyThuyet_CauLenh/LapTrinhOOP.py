"""
- Class / Đối tượng: """
class SimpleClass:
    # Attribute:
    i = 5
    # _init_
    def __init__(self):
        self.j = 7
    # Methods:
    def printMe(self):
        print(self.j)
objectA = SimpleClass()
objectB = SimpleClass()
objectA.printMe()
print(objectB.i)