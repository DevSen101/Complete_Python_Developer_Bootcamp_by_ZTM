# OOP gives us ability to write


# class PlayerCharacter:
#     def __init__(self, name, age):
#         self.name = name  # attributes
#         self.age = age  # attributes


# player1 = PlayerCharacter("Virat", 22)
# player2 = PlayerCharacter("Rohit", 23)

# print(player1.age)
# print(player2.name)


# ------------------------------
# default value to method


class PlayerCharacter:
    membership = True  # class attributes shared by all instances

    def __init__(self, name="Dhoni", age=20):
        if PlayerCharacter.membership:
            self.name = name  # Instance attributes - unique to each obj
            self.age = age  # Instance attributes

    def shout(self):
        print(f"My name is {self.name}")


player1 = PlayerCharacter("Virat", 22)
player2 = PlayerCharacter("Rohit", 23) #pass arguments
player3 = PlayerCharacter()   #uses default values

print(player1.age)
print(player2.name)
print(player3.shout())  # we can also give default value
