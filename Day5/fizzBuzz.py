# Print numbers from 1 to 100 if % 3 print fizz ,%5 print buzz , if % by 3 and % by 5 print fizzbuzz
print(" *******************\tFizz Buzz\t******************* \n")
for i in range(1, 101):
    if i % 3 == 0 and not i % 5 == 0:
        print("I would like to say Fizz !!")
    elif i % 5 == 0 and not i % 3 == 0:
        print("I would like to say Buzz !!")
    elif i % 5 == 0 and i % 3 == 0:
        print(" ** I would like to say Fizz Buzz !! **")
    else:
        print(f"I would like to say {i} !!")
