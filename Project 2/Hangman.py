# inheritence

class Car:
    def __init__(self,year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def age(self):
        return 2016 - self.year

class Mustang(Car):
    def __init__(self, year):
        self.year = year
        self.model = "Mustang"
        self.make = "Ford"
