def userName(func):
    def wrapper_function(User_name, password):
        print('******')
        func(User_name, password)
    return wrapper_function


@userName
def welcome_user(Username, password):
    print(
        f'hello {Username} and your password is {len(password)} characters long')


welcome_user('Stark', 'Mr.stark')
