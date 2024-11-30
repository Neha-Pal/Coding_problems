class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name:{self.name} Age:{self.age}")

p = Person("Neha", 22)
p.display()
