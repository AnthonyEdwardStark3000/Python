# Find the total number of paint cans required
import math

print("**************** Paint can calculator ****************")
wall_height = int(input("Enter the height of the wall in m :"))
wall_width = int(input("Enter the width of the wall in m :"))
cover = 5


def paint_Calculator(height, width, coverage):
    return math.ceil((wall_height * wall_width) / coverage)


numberOfCans = paint_Calculator(height=wall_height, width=wall_width, coverage=cover)
numberOfCans = round(numberOfCans)
print(f"The total number of cans required to paint the wall of the required params is :{numberOfCans}")
