import turtle
import random

turtle.colormode(255)

WIDTH = 1
LENGTH = 2
DISTANCE = random.randint(5, 10)
LOCATION = (270, random.randint(-240, 250))
COLOR_LIST = [(222, 152, 103), (128, 172, 199),
              (221, 130, 149), (221, 73, 90), (243, 208, 99), (17, 121, 157),
              (118, 176, 147), (34, 120, 82), (18, 165, 204), (230, 74, 70),
              (142, 86, 60), (116, 85, 102), (162, 209, 162), (13, 169, 120),
              (171, 183, 219), (177, 154, 75), (213, 222, 213), (1, 98, 119),
              (54, 61, 96), (240, 177, 165), (221, 167, 185), (146, 204, 228), (24, 98, 61)]


class Car(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color(random.choice(COLOR_LIST))
        self.shape("square")
        self.shapesize(WIDTH, LENGTH)
        self.penup()
        self.goto(LOCATION)
        self.setheading(180)

    def move_forward(self):
        self.forward(DISTANCE)
