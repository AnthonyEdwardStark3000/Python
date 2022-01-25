#Having more than one if
print("********************\tWelcome to RollerCoaster\t********************\n")
height = int(input("Please Enter your height in cms: "))
if height >= 180:
    print("You are permitted for the ride.")
    age = int(input("Enter your age : "))
    if age >= 18:
        print("You are supposed to pay 7$ ")
    else:
        print("You are supposed to pay 12$ ")
else:
    print(" Sorry You are not allowed to ride ")