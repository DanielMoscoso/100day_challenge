# TODO: 1.-Create a 600x600 screen to hold the game.
# TODO: 2.-Create individual Turtle that moves up and down.
# TODO: 3.-Create car module for individual cars crossing the road.
# TODO: 3.1.-Make the cars randomly appear on the screen.
# TODO: 3.2.-Each car should have a different color when they appear.
# TODO: 3.3.-Each car should cover a diffent amount of distance when they appear.
# TODO: 3.4.-The cars speed up as the levels increase.
# TODO: 4.-If the turtle hits a car, then it is Game Over.

from modules import car, scoreboard, timmy
from turtle import Turtle, Screen
import time


# --------------------------------- Functions ---------------------------------
def make_car():
    """
    This creates a new car and adds it to the car list.
    """
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

timmy_the_turtle = timmy.Timmy()
score = scoreboard.Scoreboard()

for _ in range(20):
    make_car()

screen.listen()
screen.onkey(timmy_the_turtle.move_up, "w")
screen.onkey(timmy_the_turtle.move_down, "s")

# Game:
repeat = True
sleep_time = 0.1
while repeat:
    screen.update()
    time.sleep(sleep_time)

    for car in car_list:
        car.move_forward()
        if car.xcor() < -290:  # Car hitting the left wall.
            car.new_location()

        if timmy_the_turtle.distance(car) < 22:  # Hitting a car.
            repeat = False
            score.game_over()

    if timmy_the_turtle.ycor() > 260:  # Finish line
        sleep_time *= 0.8  # Increase the speed of the cars.
        score.increase_score()
        score.clear()
        score.write_score()
        timmy_the_turtle.back_to_start()  # Go back to the origin.


screen.exitonclick()
