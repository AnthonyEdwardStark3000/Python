#BMI Calculator
print("********************\tWelcome to BMI CAlCULATOR\t********************\n")
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
Overall_bmi = weight / height ** 2
bmi = round(Overall_bmi, 2)
if bmi < 18.5:
    print(f"You are underweight with {bmi} bmi")
elif bmi < 25:
    print(f"You are normal weight with {bmi} bmi")
elif bmi < 30:
    print(f"You are overweight with {bmi} bmi")
elif bmi < 35:
    print(f"You are obese with {bmi} bmi")
else:
    print(f"You are clinically obese with {bmi} bmi")