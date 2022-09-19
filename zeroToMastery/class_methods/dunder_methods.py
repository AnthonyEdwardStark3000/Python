class Toy():
    def __init__(self, type, age):
        self.type = type
        self.age = age

    def __str__(self):
        return f'Hello {self.type}'


woody = Toy('cow_boy', 1)
print(dir(woody))
print(f'Dunder __str__: {woody.__str__()}')

