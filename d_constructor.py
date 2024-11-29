class Person():
    def __init__(self):
        self.name = "Neha Pal"
        self.age = 22

    def Display(self):
        print(f"Name:{self.name}  Age:{self.age}")

p = Person()
p.Display()