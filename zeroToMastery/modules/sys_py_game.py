import random
import sys

chosen_choice = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

while True:
    # print('Enter a number:')
    try:
        user_input = int(sys.argv[1])
    except ValueError as error_occurred:
        print(f'Enter a valid number as {error_occurred} error occurred')
    else:
        if chosen_choice == user_input:
            print(
                f'Done with the program as User chose {user_input} and the computer chose {chosen_choice}')
        else:
            print(
                f'Enter another number User chose {user_input} and the computer chose {chosen_choice}.')
        break
