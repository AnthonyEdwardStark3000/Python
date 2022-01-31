import random

print("\n********************* Hangman *********************\n")
words = ["encyclopedia", "moaning", "pupil", "faculty"]
display = []
lives = 0
HANGMAN_PICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

end_of_game = False
question = (random.choice(words))
print("Question is:" + question)
print(len(question))
for _ in range(len(question)):
    display += '_'
while not end_of_game:
    guess = input("Enter your input:")
    guess = guess.lower()

    for position in range(len(question)):
        # guess=question[position]
        if guess == question[position]:
            print("Correct")
            display[position] = guess

        if guess not in question:
            # print("Else part")
            print(HANGMAN_PICS[lives])
            lives += 1
            if lives == 6:
                end_of_game = True
                print("You lose")

    print(display)
    if '_' not in display:
        end_of_game = True
        print("You Win")
