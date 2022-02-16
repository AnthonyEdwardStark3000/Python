# Snake game from Nokia
from turtle import Screen
from snake import Snake
from Food import Food
from ScoreBoard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Nokia Snake")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
gameOn = True

while gameOn:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Collision with the Food
    if snake.head.distance(food) < 15:
        food.RefreshFood()
        scoreboard.increase_score()

screen.exitonclick()
