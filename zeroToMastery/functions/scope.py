# Scope - Accessibility of a function or variable.
name = 'Suresh' # Global scope

if True: # This creates global scope.
    age = 22

def display_name():
    name = 'Mr.Stark' # Functional scope .
    age = 10
    print(f"I am {name} and am {age} years old.")

display_name()
print(f"And My name is {name} and am {age} years old.")