# TODO: 1.-Create a 600x600 screen to hold the game.
# TODO: 2.-Create individual Turtle that moves up and down.
# TODO: 3.-Create car module for individual cars crossing the road.
# TODO: 4.-Make the cars randomly appear on the screen.
# TODO: 5.-Each car should have a different color when they appear.
# TODO: 6.-The cars speed up as the levels increase.
# TODO: 7.-If the turtle hits a car, then it is Game Over.

from modules import cars
from turtle import Turtle, Screen
import time


# --------------------------------- Functions ---------------------------------
def move_up():
    timmy.forward(20)


def move_down():
    timmy.backward(20)
# --------------------------------- Functions ---------------------------------


# Initialization:
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Cross the road")
# screen.tracer(0)

timmy = Turtle("turtle")
timmy.color("blue")
timmy.speed(0)
timmy.penup()
timmy.setheading(90)
timmy.goto(0, -280)

screen.listen()
screen.onkey(move_up, "w")
screen.onkey(move_down, "s")

# screen.update()
# time.sleep(0.1)

screen.exitonclick()
