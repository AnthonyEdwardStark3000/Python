print(" *******************\tHighest Mark\t******************* ")
studentCount = int(input("Enter the total number of students count you want to enter: "))
markList = []
for i in range (0, studentCount):
    mark = float(input("Enter the mark :"))
    markList.append(mark)
print(f"The maximum mark from the entered marks is {max(markList)}")
