#Having more than one if
print("********************\tWelcome to RollerCoaster\t********************\n")
height = int(input("Please Enter your height in cms: "))
if height >= 180:
    print("You are permitted for the ride.")
    age = int(input("Enter your age : "))
    if age <= 12:
        bill = 5
        print(f"Children tickets are {bill}$")
    elif age >= 18:
        bill = 7
        print(f"Youth tickets are {bill}$ ")
    else:
        bill = 12
        print(f"Adult tickets are {bill}$ ")
    photo = input("Do you want to take photos? y for yes n for no: ")
    if photo == "y":
        bill += 3
    print(f"Your final payable amount after photo conformation is :{bill}$")

else:
    print(" Sorry You are not allowed to ride ")