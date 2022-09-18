class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def self_introduction(self):
        print(f'The player name is{self.name} and he is {self.age} years old.')


p1 = Player('Jarvis', 22)
p1.self_introduction()
