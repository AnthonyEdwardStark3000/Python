class numbers:
    def __init__(self, name, number):
        print(f'{name} entered the number {number}')

    @classmethod
    def enter_number(cls, name, entered_number):
        cls(name, entered_number)
        return 'Done with the functions'

    @staticmethod
    def check(variable):
        print(f'The string {variable} is entered for checking')
        return 'And the value is appended perfectly.'


print(numbers.enter_number('Suresh', 3000))
print(numbers.check('Suresh'))
