def leapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def daysInMonth(year, month):
    if month > 12 or month < 1:
        return "invalid input entered"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 30, 30, 31]
    if leapYear(year) and month == 2:  # checking for leap year
        return 29
    else:
        return month_days[month - 1]


print(" ************** Days calculator **************")
yr = int(input("Enter the year :"))
mn = int(input("Enter the Month :"))
days = daysInMonth(year=yr, month=mn)
print(f"\nThe Month {mn} of the Year {yr} has '{days}' in it.")
