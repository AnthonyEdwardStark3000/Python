# Turtle race predictor
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Decision Maker", prompt="Enter who's gonna win the race")
print(user_choice)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
x_value = -230
y_value = -100
is_RaceOn = False
all_turtles = []
for colour in colors:
    my_turtle = Turtle(shape="turtle")
    my_turtle.penup()
    my_turtle.shape()
    my_turtle.color(colour)
    my_turtle.goto(x=x_value, y=y_value)
    y_value += 30
    all_turtles.append(my_turtle)
if user_choice:
    is_RaceOn = True
while is_RaceOn:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_RaceOn = False
            winner = turtle.pencolor()
            if winner == user_choice:
                print("Hurray ! you won the match")
            else:
                print(f"You lose , winner is {winner} turtle")
        turtle.forward(random.randint(0, 10))
screen.exitonclick()
