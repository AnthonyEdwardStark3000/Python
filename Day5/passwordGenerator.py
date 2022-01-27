print(" *******************\tPassword Generator\t******************* \n")
import random

letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
    "x", "y", "z"
]
numbers = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]
characters = [
    "!", "@", "#", "$", "%", "^", "&", "*", "/", "?", "|", ":"
]
letters_Count = int(input("\tEnter the number of letters you want in your password :"))
numbers_Count = int(input("\tEnter the number of numbers you want in your password :"))
characters_Count = int(input("\tEnter the number of characters you want in your password :"))
password = ""
chosen_letters = ""
chosen_numbers = ""
chosen_characters = ""
for i in range(1, letters_Count + 1):
    chosen_letters += random.choice(letters)
# print(chosen_letters)

for i in range(1, numbers_Count + 1):
    chosen_numbers += random.choice(numbers)
# print(chosen_numbers)

for i in range(1, characters_Count + 1):
    chosen_characters += random.choice(characters)
# print(chosen_characters)

password = chosen_letters+chosen_characters+chosen_numbers
print(f"\tYour password could be :{password}")