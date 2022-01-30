# Hangman game
import random

words_list = ["Ganesh", "Vinayak", "Murugan"]
chosen_word = random.choice(words_list)
word = chosen_word.lower()
print(word)
display = []
for i in range(0, len(word)):
    display += "_"
print(display)

guess = input("Enter any word to check :")
for i in range(len(chosen_word)):
    letter = chosen_word[i]
    if letter == guess:
        display[i] += letter
        print(display)
    # else:
    #     # print(letter)
    #     print("Incorrect choice")