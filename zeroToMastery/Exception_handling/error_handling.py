while True:
    try:
        age = int(input('Enter your age in numbers:'))
        # print(f'Cant believe that you are {age} years old')
        10 / age
    except ValueError:
        print('Invalid input , plz enter a valid number')
    except ZeroDivisionError:
        print('Please enter a age that is not zero')
    else:
        print('Nice meeting you.')
        break
