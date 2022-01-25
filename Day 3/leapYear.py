#Leap year
#should be evenly divisible by 4
#not with 100
#but with 400
year = int(input("Enter an year to checK :"))
if year % 4 ==0:
    if year % 100 ==0:
        if year % 400 ==0:
            print(f"Year {year} is an leap  year")
        else:
            print(f"Year {year} is not an leap  year")
    else:
        print(f"Year {year} is an leap  year")
else:
    print(f"Year {year} is not an leap  year")