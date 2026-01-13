# Multiple inheritance in Python allows a class to inherit from more than one parent class simultaneously.

class Parent1:
    def method1(self):
        print("From Parent1")

class Parent2:
    def method2(self):
        print("From Parent2")

class Child(Parent1, Parent2):  # Inherits from both
    pass

vinod = Child()
print(vinod)