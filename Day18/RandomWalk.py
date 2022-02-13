# random directional walk
import turtle as t
import random

tut = t.Turtle()
tut.shape("circle")
tut.speed("fastest")
t.colormode(255)

directions = [0, 90, 180, 270]


def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for _ in range(500):
    tut.color(randomColor())
    tut.pensize(12)
    tut.forward(30)
    tut.setheading(random.choice(directions))
