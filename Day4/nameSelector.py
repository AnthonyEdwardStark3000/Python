# Select name from the lists
import random

name_String = input("Enter the name of your friends with , separating each :")
name = name_String.split(", ")
payer_name = random.randint(0, len(name)-1)
print(f"The person named {name[payer_name]} is going to pay the bill today")
