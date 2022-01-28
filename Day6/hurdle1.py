def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    turn_left()
    turn_right()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
move()
for i in range(1, 6):
    jump()
    move()
jump()    