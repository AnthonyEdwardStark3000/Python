from random import randint

answer = randint(1, 10)
while True:
    user_input = input('Enter a number between 1 and 10 :')
    try:
        if int(user_input) > 0 and int(user_input) < 11:
            if int(user_input) == answer:
                print(
                    f'You won you chose {user_input} and the computer chose {answer}')
                break
            else:
                print(
                    f'You lost you chose {user_input} and the computer chose {answer}')
        else:
            print('Hey enter a number between 1 and 10')
    except ValueError as err:
        print(f'Please enter a valid number {err} occurred')
        continue
