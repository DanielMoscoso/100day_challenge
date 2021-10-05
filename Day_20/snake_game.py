from turtle import Turtle, Screen
import time
from modules import snake
import os
os.chdir('C:\\Users\\Daniel\\Documents\\Python\\100days\\Day_20')

# TODO: 1.-Create a snake body.
# TODO: 2.-Move the snake.
# TODO: 3.-Control the snake.
# TODO: 4.-Detect collision with food.
# TODO: 5.-Create a scoreboard.
# TODO: 6.-Detect collision with wall.
# TODO: 7.-Detect collision with tail.

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = snake.Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
