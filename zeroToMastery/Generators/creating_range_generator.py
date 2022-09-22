class Myrange():
    current_number = 0

    def __init__(self, starting, ending):
        self.starting = starting
        self.ending = ending

    def __iter__(self):
        return self

    def __next__(self):
        if Myrange.current_number < self.ending:
            num = Myrange.current_number
            Myrange.current_number += 1
            return num
        raise StopIteration


gen = Myrange(0, 10)
for i in gen:
    print(i)
