#  Calculator using Dictionaries and functions
#   Addition

def add(num1, num2):
    return num1 + num2


#   Subtraction


def sub(num1, num2):
    return num1 - num2


#   Multiplication

def mul(num1, num2):
    return num1 * num2


#   Division


def div(num1, num2):
    return num1 / num2


decision = True

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}
print("**************** Calculator ****************")
number1 = int(input("Enter the first Number :"))

for symbol in operations:
    print(symbol)

while decision:
    operation = input("Enter the operation that you want to perform :")
    number2 = int(input("Enter the next Number :"))
    calculation_function = operations[operation]
    answer = calculation_function(num1=number1, num2=number2)
    print(f"The result after performing the {operation} on {number1} and {number2} is : {answer}")
    continueOperation = input("Enter whether you want to continue :")
    if continueOperation == 'n' or continueOperation == 'N':
        decision = False
    else:
        operation = input("Enter another operation that you want to perform :")
        number3 = int(input("Enter another number :"))
        calculation_function = operations[operation]
        answer1 = calculation_function(num1=answer, num2=number3)
        print(f"The answer received  after performing {operation} operation on {answer} and {number3} is {answer1}")
        continueOperation = input("Enter whether you want to continue :")
        if continueOperation == 'n' or continueOperation == 'N':
            decision = False
