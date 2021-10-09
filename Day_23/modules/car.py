from turtle import Turtle

WIDTH = 1
LENGTH = 2


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color("red")
        self.shape("square")
        self.shapesize(WIDTH, LENGTH)
        self.penup()
        self.goto(270, 0)
        self.setheading(180)
