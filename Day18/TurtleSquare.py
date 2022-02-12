# Creating square with turtle
from turtle import Turtle, Screen


def square(turtle_color):
    colour = turtle_color
    my_turtle.forward(100)
    my_turtle.color(colour)
    my_turtle.right(90)
    my_turtle.color(colour)


my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("violet")

colors = ["Red", "blue", "violet", "grey"]
for color in colors:
    square(turtle_color=color)

screen = Screen()
screen.exitonclick()
