#BMI Calculator
height = float(input("Please enter your height in m:"))
weight = float(input("Please enter your weight in kg:"))
bmi = weight / height ** 2
print(round(bmi ,2)) #rounding to two decimal places
