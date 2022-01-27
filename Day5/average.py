# Finding the average height from the entered list
print(" *******************\tAverage Height\t******************* ")
count = int(input("Enter the total number of students :"))
student_height = []
total_height = 0
average_height = 0
for i in range(0, count):
    height = input("Enter the height of the student :")
    student_height.append(height)
for i in student_height:
    total_height += float(i)
    # print(total_height)
average_height = total_height / len(student_height)
print(f"The average height of the entered student's list is {average_height} m")
