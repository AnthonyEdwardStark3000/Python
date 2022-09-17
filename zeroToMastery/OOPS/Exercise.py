'''
# Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats



# 2 Create a function that finds the oldest cat



# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
'''


from gettext import find


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


adam = Cat("Adam", 4)
felix = Cat("Felix", 3)
santo = Cat("Santo", 8)


def max_age(*args):
    return max(args)


print(
    f'The cat with the highest age is : {max_age(adam.age,felix.age,santo.age)}')
