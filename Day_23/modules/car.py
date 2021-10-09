from turtle import Turtle
import random

WIDTH = 1
LENGTH = 2
DISTANCE = random.randint(5, 10)
LOCATION = (270, random.randint(240, 250))


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color("red")
        self.shape("square")
        self.shapesize(WIDTH, LENGTH)
        self.penup()
        self.goto(LOCATION)
        self.setheading(180)

    def move_forward(self):
        self.forward(DISTANCE)
