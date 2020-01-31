# Classes and variables
# init

class Dog:

    def __init__(self, name, age, furcolor):
        self.name = name
        self.age = age
        self.furcolor = furcolor

    def barkhello(self):
        print("Hello World")


dog1 = Dog("Fido", 8, "Brown")
dog1.barkhello()

print(dog1.furcolor)

class Car:
    def __init__(self,year, make, model):
        self.year = year
        self.make = make
        self.model = model
        self.age = 2019 - year

car1 = Car(1981, "Audi", "80")
