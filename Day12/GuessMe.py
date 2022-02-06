# Guess the randomly generated number from 1 to 100
import random

logo = """

 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |    ______    | || | _____  _____ | || |  _________   | || |    _______   | || |    _______   | || |              | || | ____    ____ | || |  _________   | |
| |  .' ___  |   | || ||_   _||_   _|| || | |_   ___  |  | || |   /  ___  |  | || |   /  ___  |  | || |              | || ||_   \  /   _|| || | |_   ___  |  | |
| | / .'   \_|   | || |  | |    | |  | || |   | |_  \_|  | || |  |  (__ \_|  | || |  |  (__ \_|  | || |              | || |  |   \/   |  | || |   | |_  \_|  | |
| | | |    ____  | || |  | '    ' |  | || |   |  _|  _   | || |   '.___`-.   | || |   '.___`-.   | || |              | || |  | |\  /| |  | || |   |  _|  _   | |
| | \ `.___]  _| | || |   \ `--' /   | || |  _| |___/ |  | || |  |`\____) |  | || |  |`\____) |  | || |              | || | _| |_\/_| |_ | || |  _| |___/ |  | |
| |  `._____.'   | || |    `.__.'    | || | |_________|  | || |  |_______.'  | || |  |_______.'  | || |   _______    | || ||_____||_____|| || | |_________|  | |
| |              | || |              | || |              | || |              | || |              | || |  |_______|   | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
                                                
                                                  
"""
print(logo)
print("<<< Welcome to the Number Guessing Game >>>\nI am thinking of a number between 1 and 100.")
life = 0
difficulty = input("Choose a difficulty .Type 'easy' or 'hard' :").lower()
if difficulty == 'easy':
    life = 10
elif difficulty == 'hard':
    life = 5
number = random.randint(1, 101)


def result(number_chosen, life_left):
    while life_left > 0:
        print(f"You have {life_left} remaining attempts to guess the number")
        user_input = int(input("Make a Guess :"))
        if user_input > number_chosen:
            print("Too high")
            print("Guess Again")
        elif user_input < number_chosen:
            print("Too low\n Guess Again")
        elif user_input == number_chosen:
            print("You won !")
            break
        life_left -= 1
        if life_left == 0:
            print(f"Sorry you ran out of lives and the answer is : {number_chosen}")


result(number_chosen=number, life_left=life)
restart = input("Do you want to restart the game ?\n Press Y for Yes and N for no :").lower()
if restart == 'y':
    result(number_chosen=number, life_left=life)
else:
    print("Thank you")