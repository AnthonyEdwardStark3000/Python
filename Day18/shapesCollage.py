# Hint an complete rotation takes 360 degree
import turtle as t
import random

turt = t.Turtle()
colors = ["violet", "yellow", "419f6a","red","green","pink","SeaGreen","DarkOrchid","CornflowerBlue","DeepSkyBlue"]

def drawShape(numberOfSides):
    degree = 360 / numberOfSides
    for _ in range(numberOfSides):
        turt.forward(100)
        turt.right(degree)


for i in range(3, 11):
    turt.color(random.choice(colors))
    drawShape(numberOfSides=i)
