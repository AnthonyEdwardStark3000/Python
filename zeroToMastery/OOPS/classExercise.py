class PlayerCharacter:
    def __init__(self, name):
        self.age = int(input('Enter your age :'))
        print(f'Welcome {name}')

    def run(self, name):
        print(
            f'Running in action by {name} and is running faster than {self.age} in years')


suresh = PlayerCharacter(name='Mr.Stark')
suresh.run('Mr.Stark')

babu = PlayerCharacter(name='Jarvis')
babu.run('JARVIS')
