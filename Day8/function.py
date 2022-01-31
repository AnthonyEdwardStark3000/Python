# Functions in action
def greet():
    print("hi\nHola\nWelcome")


def greets(name):
    print(f"Hello {name}")
    print("How are you doing ?")


def greets_With(name, location):
    print(f"Hello {name}")
    print(f"Whats the weather at {location}?")


print("The day 8 begins with")
greet()
greets("Mr.Stark")
greets_With(location="USA", name="Mr.Stark")
