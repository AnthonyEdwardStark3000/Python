class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f'Welcome\t:{self.name}')

    @classmethod
    def adding_things(cls, number1, number2):
        return number1+number2


print(PlayerCharacter.adding_things(10, 90))
