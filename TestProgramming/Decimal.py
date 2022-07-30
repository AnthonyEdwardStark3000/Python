print("Enter the decimal number:")
decimalNumber =int(input())
if decimalNumber <= 0:
    print("Invalid Input")
else:
    binaryNumber = bin(decimalNumber)[2:]
    print(f"The binary equivalent of decimal number {decimalNumber} is {binaryNumber}")