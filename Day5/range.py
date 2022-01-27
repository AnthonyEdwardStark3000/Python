#Range will take upto target -1 size so add an incremented value
print(" *******************\tRange\t******************* \n")
number = 0
for i in range(1, 101): #finding the number by adding numbers from 1 to 100
    number += i
print(f"After adding numbers from 1 to 100 answer is :{number}")

number = 0
for i in range(1, 101, 2):#finding the number by adding numbers from 1 to 100 incrementing by 2
    number += i
print(f"After adding numbers from 1 to 100 answer is :{number}")