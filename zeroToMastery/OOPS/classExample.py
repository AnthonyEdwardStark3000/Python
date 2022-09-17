class SelfIntro:
    def __init__(self):
        self.Name = input('Enter your name:')
        self.Age = int(input('Enter your Age:'))
        self.resume()

    def resume(self):
        print(f'Hello Mr.{self.Name}')


Zoho = SelfIntro()
Apple = SelfIntro()

Zoho.isAppointed = True

print(Zoho.isAppointed)
print(Apple.isAppointed)
