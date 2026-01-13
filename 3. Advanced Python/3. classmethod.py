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
player3 = PlayerCharacter.adding_things(5, 6)
print(player3)

# ---------------------------------------
