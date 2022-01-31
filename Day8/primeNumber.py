# Checking whether an number is prime or not
number = int(input("Enter any number : "))


def checker(num):
    flag = 0
    for i in range(1, num):
        if num % i == 0:
            flag += 1
            print(f"Check {i}")
    if flag == 1:
        print(f"The entered number {number} is an prime number")
    else:
        print(f"The entered number {number} is not an prime number")


checker(number)
