# TODO: 1.-Create a 600x600 screen to hold the game.
# TODO: 2.-Create individual Turtle that moves up and down.
# TODO: 3.-Create car module for individual cars crossing the road.
# TODO: 3.1.-Make the cars randomly appear on the screen.
# TODO: 3.2.-Each car should have a different color when they appear.
# TODO: 3.3.-Each car should cover a diffent amount of distance when they appear.
# TODO: 3.4.-The cars speed up as the levels increase.
# TODO: 4.-If the turtle hits a car, then it is Game Over.

from modules import car, scoreboard
from turtle import Turtle, Screen
import time


# --------------------------------- Functions ---------------------------------
def move_up():
    timmy.forward(20)


def move_down():
    timmy.backward(20)


def make_car():  # COMBAK: Implement
    new_car = car.Car()
    car_list.append(new_car)
# --------------------------------- Functions ---------------------------------


# Initialization:
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Cross the road")
screen.tracer(0)
car_list = []

timmy = Turtle("turtle")
timmy.color("blue")
timmy.speed(0)
timmy.penup()
timmy.setheading(90)
timmy.goto(0, -280)

score = scoreboard.Scoreboard()
for _ in range(10):
    make_car()

screen.listen()
screen.onkey(move_up, "w")
screen.onkey(move_down, "s")

repeat = True
while repeat:
    screen.update()
    # time.sleep(0.1)
    time.sleep(0.001)

    for car in car_list:
        car.move_forward()
        if car.xcor() < -290:
            car.new_location()

        if timmy.distance(car) < 25:
            score.game_over()
            repeat = False

    if timmy.ycor() > 260:
        score.increase_score()
        score.clear()
        score.write_score()
        timmy.goto(0, -280)  # Go back to the origin.

screen.exitonclick()
