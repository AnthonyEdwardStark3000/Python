#Calculating the sum of even numbers from 1 to 100
print(" *******************\tEven Numbers\t******************* \n")
number = 0
for i in range (0, 101, 2):
    number += i
print(f"The sum of the even numbers from the range 0 to 100 is :{number}")