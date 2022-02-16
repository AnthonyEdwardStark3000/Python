# Simple program to check multiple Inheritance
class Number:
    def __init__(self):
        self.starting_number = 0

    def add(self):
        print("starting_number")


class MyNumber(Number):
    def __init__(self):
        super().__init__()
        starting_number = 10
        print(starting_number)


two = MyNumber()
two.add()
print(two.starting_number)