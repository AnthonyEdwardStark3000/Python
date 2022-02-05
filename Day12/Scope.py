# Global Scope
print("\n********************************** Scopes of the variables **********************************")
number = 1


def sample():
    number = 100
    print(f"Inside the function the number is {number}")


print(f"Outside the function the number is {number}")
print("Calling the function ...")
sample()

# No block scope

print("\n********************************** No block Scope **********************************")
Languages_list = ["React js", "Ionic", "Express js", "Angular", "Bug Bounty"]
languages_known = 2
if languages_known <= 3:
    next_language = Languages_list[0]
    print(f"You should next move to {next_language}")
print(f"Calling outside the if block.....\n Should next study {next_language}")

print("\n********************************** No block Scope But Function has scope **********************************")


def next_study():
    program_list = ["React js", "Ionic", "Express js", "Angular", "Bug Bounty"]
    programs_known = 2
    if programs_known <= 3:
        next_study = Languages_list[0]
        print(f"You should next study {next_study} it has scope")


print(f"Calling outside the if block.....\n Should next study {next_study}")
print("Accessing outside the function receives an error...")

print("\n********************************** Modifying Global scope variables **********************************")
print(f"The global value of the number is :{number}")


def increment_number():
    global number
    number += 100
    print(f"The value  of the global variable after addition inside a function is : {number}")


print(f"Using global keyword to modify the global variable")
increment_number()
print("\n**********************************  Global Constant variables **********************************")
PI = 3.14
print("They all should be Uppercase letters for mentioning them as constants")
print(f"The value of the constant variable Pi is :{PI}")
