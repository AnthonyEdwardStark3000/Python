# Functions
def format_Name(first, last):
    if first == "" or last == "":
        return "You haven't provided any valid data"
    formatted_Fname = first.title()
    formatted_Lname = last.title()
    return f"Your name is {formatted_Fname} {formatted_Lname}"


firstName = input("Enter your first name :")
lastName = input("Enter your last name :")
print(format_Name(first=firstName, last=lastName))
