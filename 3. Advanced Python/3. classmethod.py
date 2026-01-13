class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name  # attributes
        self.age = age  # attributes

    def shout(self):
        print(f"My name is {self.name}")

    @classmethod
    def adding_things(cls, n1, n2):
        return cls("Tedy", n1 + n2)

    @staticmethod
    def adding_things2(n1, n2):
        return n1 + n2


# player1 = PlayerCharacter("Virat", 20)
# print(player1.adding_things(2, 3))
# player3 = PlayerCharacter.adding_things(5, 6)
# print(player3)

# ---------------------------------------

# ex2


class Car:
    wheels = 4  # CLASS ATTRIBUTE - all cars have 4 wheels

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def honk(self):  # REGULAR METHOD
        print(f"{self.brand} says BEEP BEEP!")

    @classmethod
    def from_age(cls, age):  # CLASS METHOD - factory special!
        year = 2026 - age  # current year - age
        return cls("Toyota", year)

    @staticmethod
    def fuel_price(liters):  # STATIC METHOD - just calculator
        return liters * 100


# TRY IT OUT!
car1 = Car('BMW', 2017)  # Factory makes 5-year-old car!
print(car1.brand)  # Toyota
print(car1.year)  # 2021
age = Car.from_age(22)
print(age)
car1.honk()  # Toyota says BEEP BEEP!

price = Car.fuel_price(10)  # Just calculator
print(price)  # 1000 rupees
