# In matrix format
row1 = ["one", "two", "three"]
row2 = ["four", "five", "six"]
row3 = ["seven", "eight", "nine"]
common_row = [row1, row2, row3]
print(f"{row1}\n {row2}\n {row3}\n")
place = input("Enter the place to put the treasure :")
horizontal = int(place[0])
vertical = int(place[1])
selected_row = common_row[horizontal-1]
selected_row[horizontal] = "x"
print(common_row)