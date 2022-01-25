# Having more than one if
print("********************\tWelcome to RollerCoaster\t********************\n")
flag = 0
bill = 0
height = int(input("Please Enter your height in cms: "))
if height >= 180:
    print("You are permitted for the ride.")
    age = int(input("Enter your age : "))
    if age <= 12:
        bill = 5
        print(f"Children tickets are {bill}$")
        flag = 1
    elif age <= 18:
        bill = 7
        print(f"Youth tickets are {bill}$ ")
        flag = 1
    elif age > 18 and age < 45:
        bill = 12
        print(f"Adult tickets are {bill}$ ")
        flag = 1
    elif age <= 45 and age <= 55:
        bill = 0
        print(f"You can enjoy your jolly ride for {bill}$")
        flag = 1
    else:
        print("Sorry you are too old to have an roller coaster trip! ")
    if flag == 1:
        photo = input("Do you want to take photos? y for yes n for no: ")
        if photo == "y":
            bill += 3
    else:
        print("Thank you")
    print(f"Your final payable amount after photo conformation is :{bill}$")

else:
    print(" Sorry You are not allowed to ride ")
