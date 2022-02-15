# Snake game from Nokia
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Nokia Snake")
screen.tracer(0)
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for position in starting_positions:
    snake = Turtle()
    snake.shape("square")
    snake.color("white")
    snake.penup()
    snake.goto(position)
    segments.append(snake)
gameOn = True
while gameOn:
    screen.update()
    time.sleep(0.1)
    for segment_number in range(len(segments)-1, 0, -1):
        newX = segments[segment_number-1].xcor()
        newY = segments[segment_number - 1].ycor()
        segments[segment_number].goto(newX, newY)
    segments[0].forward(20)
    segments[0].left(90)
screen.exitonclick()
