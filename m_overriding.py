class Animal:
    def speak(self):
        print('Make sound')
    
class Dog(Animal):
    def speak(self):
        print('Dog barks')

class Cat(Animal):
    def speak(self):
        print('Cat meows')

d = Dog()
c = Cat()

d.speak()
c.speak()