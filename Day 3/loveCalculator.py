#Read two names add them and count letters true , love and concatenate them
print("*****************\t Welcome to Love Calculator \t*****************")
yourName = input("Enter your name: ")
herName = input("Enter her name: ")
combinedName = yourName+ herName
combinedName = combinedName.lower()
print(combinedName)
t = combinedName.count("t")
r = combinedName.count("r")
u = combinedName.count("u")
e = combinedName.count("e")
true = t+r+u+e
true =str(true)
l = combinedName.count("l")
o = combinedName.count("o")
v = combinedName.count("v")
e = combinedName.count("e")
love = l+o+v+e
love =str(love)
percentage = true+ love
percentage = int(percentage)
if(percentage <10) or (percentage>90):
    print(f"{percentage} is coke and mentos")
elif (percentage >=40) and (percentage <=50):
    print(f"{percentage} Percentage is alright")
else:
    print(f"You have scored {percentage} percentage")
