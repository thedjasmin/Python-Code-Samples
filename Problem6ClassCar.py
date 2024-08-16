# Jasmin Duishebaeva
# 08.15.2024

# Problem 6: Modify the car class to include 'type' and 'manufacturer' attributes.

class Car:

    def __init__(self, model, year, color, car_type, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.car_type = car_type
        self.manufacturer = manufacturer

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_type(self):
        return self.car_type

    def get_manufacturer(self):
        return self.manufacturer

    def fullspecs(self):
        return f"{self.manufacturer} {self.car_type} {self.model} {self.year} {self.color}"

car1 = Car("Sports", 2012, "Blue", "Coupe", "BMW")
car2 = Car("Sedan", 2020, "Black", "Saloon", "Mercedes-Benz")

print(car1.get_color())
print(car1.get_model())
print(car2.get_color())
print(car1.fullspecs())
print(car2.fullspecs())
