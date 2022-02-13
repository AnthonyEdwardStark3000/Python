# Spirograph using turtle
import turtle as t
import random

turt = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


turt.speed("fastest")


def draw_spirograph(sizeOfGap):
    for _ in range(int(360 / sizeOfGap)):
        # current_heading = turt.heading()
        turt.color(random_color())
        turt.circle(100)
        turt.setheading(turt.heading() + sizeOfGap)
        turt.circle(100)


draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()
