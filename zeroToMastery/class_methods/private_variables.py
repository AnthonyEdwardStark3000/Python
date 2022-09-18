class MyName:
    def __init__(self, name):
        self._Name = name
        self.print_my_name()

    def print_my_name(self):
        self._Name = 'Sarvesh'
        print(f'My name is :{self._Name}')


MyName('Suresh')
