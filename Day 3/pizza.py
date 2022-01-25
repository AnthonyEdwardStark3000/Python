print("*********************\tWelcome to python pizza\t*********************\n")
size = input("Enter your pizza s for small , m for medium , l for large :")
if size == "s":
    price = 10
if size == "m":
    price = 15
else:
    price = 20
pepperoni = input("Do you wish pepperoni toppings? \n y for yes n for no:")
if pepperoni == "y":
    price += 2
extraCheese = input("Do you wish to add extra cheese ?\n y for yes n for no:")
if extraCheese == "y":
    price += 3
print(f"After all those stuff you are supposed to pay {price}$ for your pizza sir")

