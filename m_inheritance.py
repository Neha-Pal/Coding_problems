class Animal:
    def desc(self):
        print('Animals')

class Dog(Animal):
    def eat(self):
        print('Dog eats Meat')

class Goat(Animal):
    def eat(self):
        print('Goat eats grass')

d = Dog()
g = Goat()
d.desc()
d.eat()
g.eat()