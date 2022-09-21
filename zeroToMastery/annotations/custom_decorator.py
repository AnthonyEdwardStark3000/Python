def my_decorator(func):
    def wrapper_function():
        print('*************')
        func()
        print('*************')
    return wrapper_function


@my_decorator
def hello():
    userName = input('Enter your name please :')
    print(f'Welcome {userName}')


@my_decorator
def bye():
    print('Bye.')


# hello()
bye()
