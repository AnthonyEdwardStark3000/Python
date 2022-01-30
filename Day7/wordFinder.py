# Hangman game
import random

words_list = ["Ganesh", "Vinayak", "Murugan"]
chosen_word = random.choice(words_list)
word = chosen_word.lower()
print(word)
guess = input("Enter any word to check :")
for i in chosen_word:
    if i == guess:
        print("Correct choice")
    else:
        print("Incorrect choice")