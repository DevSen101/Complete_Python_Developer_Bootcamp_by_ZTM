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


class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        if PlayerCharacter.membership:
            self.name = name  # attributes
            self.age = age  # attributes

    def shout(self):
        print(f'My name is {self.name}')        


player1 = PlayerCharacter("Virat", 22)
player2 = PlayerCharacter("Rohit", 23)

print(player1.age)
print(player2.name)
print(player1.shout())
