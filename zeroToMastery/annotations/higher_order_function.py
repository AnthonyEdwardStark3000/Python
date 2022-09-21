# Returning function
def greet():
    def say_hello():
        print("Hello")
    return say_hello


check = greet()
check()

# Reading function as an argument


def username():
    name = input('Enter your name :')
    print(f'Welcome {name}')


def hello(username):
    username()


hello(username)
