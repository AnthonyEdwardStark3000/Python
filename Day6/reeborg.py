#Reeborgs world
#visit https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json#
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def circle():
    move()
    turn_right()
    turn_left()
    turn_right()
def box():
    turn_left()
    circle()
    circle()
    circle()
    move()
