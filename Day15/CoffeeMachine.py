# Coffee machine program
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

Money = 0
quarter = 0.25
penny = 0.01
dime = 0.10
nickel = 0.05


def coffee():
    choice = input("What would you like to have :(espresso/latte/cappuccino ?) ").lower()
    if choice == 'report':
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${Money}")
    else:
        print("\nPlease Insert Coins: ")
        quarter_count = int(input("How Many quarters ? :"))
        dime_count = int(input("How Many dimes ? :"))
        nickel_count = int(input("How Many Nickels ? :"))
        penny_count = int(input("How Many Pennies ? :"))
        total_money = (quarter_count * quarter) + (dime_count * dime) + (nickel_count * nickel) + (penny_count * penny)
        print(round(total_money, 2))
        total_money = round(total_money, 2)
        if total_money > MENU[choice]['cost']:
            # print(MENU[choice]['cost'])
            print(f"Here is $ {total_money - MENU[choice]['cost']} in change .")
            print(f"Here is your {choice} Enjoy !")
            if MENU[choice] == 'espresso':
                resources['water'] = resources['water'] - MENU[choice]["ingredients"]['water']
                # resources['milk'] = resources['milk']
                resources['coffee'] = resources['coffee'] - MENU[choice]["ingredients"]['coffee']
            else:
                resources['water'] = resources['water'] - MENU[choice]["ingredients"]['water']
                resources['milk'] = resources['milk'] - MENU[choice]["ingredients"]['milk']
                print(resources['milk'])
                resources['coffee'] = resources['coffee'] - MENU[choice]["ingredients"]['coffee']

    if resources['water'] <= 0 or resources['milk'] <= 0 or resources['coffee'] <= 0:
        print("Money returned")
        exit()


while True:
    print(resources['water'])
    coffee()
