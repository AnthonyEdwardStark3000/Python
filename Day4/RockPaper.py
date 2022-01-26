# Game
import random

print("******************** Rock Paper Scissor ********************")
Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = [Rock, Paper, Scissor]
User_choice = int(input("\t0 for Rock \n\t1 for paper\n\t2 for scissor \n\tEnter your choice : "))
machine_choice = random.randint(0, 2)
print(machine_choice)
if User_choice == 0 and machine_choice == 2:
    print(f"User wins with {options[User_choice]} computer chose {options[machine_choice]}")

elif User_choice > machine_choice:
    if User_choice == 2 and machine_choice == 0:
        print(f"Machine wins with {options[machine_choice]} you chose {options[User_choice]}")
    else:
         print(f"User wins with {options[User_choice]} computer chose {options[machine_choice]}")

elif User_choice == machine_choice:
    print(f"Draw , computer also chose {options[machine_choice]}")

elif machine_choice > User_choice:
    print(f"Computer wins with {options[machine_choice]} you chose {options[User_choice]}")
