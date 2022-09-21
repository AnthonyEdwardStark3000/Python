# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': True
}

user2 = {
    'name': 'Dummie',
    # changing this will either run or not run the message_friends function.
    'valid': False
}


def authenticated(fn):
    def wrapper_function(*args, **kwargs):
        if dict(*args)['valid']:
            print(f'Validation is completed and you are an valid user')
            fn(*args, **kwargs)
        else:
            print("Invalid user")
    return wrapper_function


@authenticated
def message_friends(user):
    print('Sending the message ..')
    print('message has been sent')


message_friends(user2)
