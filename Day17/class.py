# Creating a class
class Myself:
    name = "Suresh"
    age = 21
    Qualification = "MCA Aspirant"
    Goals = ['Entrepreneur', 'Programmer', 'Ethical Hacker', 'Businessman', "Genius", "Billionaire"]


print("Printing the basic details about Myself")
Me = Myself()
print(f"Me {Me.name} of {Me.age} want to become an {Me.Goals[0]}, {Me.Goals[1]} ,{Me.Goals[2]} , {Me.Goals[3]},"
      f" {Me.Goals[4]} and an {Me.Goals[5]}")


class Car:
    seats = 6

    def __init__(self):
        seats = 5
        print("Seats")

    def RaceMode(self):
        seats = 2
        return seats


driver = Car()
print(f"Normally my car has {driver.seats} seats")
print(f"When I get into Race Mode it has {driver.RaceMode()} seats")
