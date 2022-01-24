#Will say the number of days weeks months left in your life
print("********* Welcome to life calculator *********\n")
age = int(input("Please enter your current age :\n"))
years_left = 92 - age
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365
print(f"You have got almost {years_left} years left \n\n {weeks_left} weeks left\n\n i.e {months_left} months left\n\n or {days_left} Days left\n\n So use it wisely")
