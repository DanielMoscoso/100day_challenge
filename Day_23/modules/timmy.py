from turtle import Turtle


class Timmy(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color("blue")
        self.speed(0)
        self.penup()
        self.setheading(90)
        self.goto(0, -280)


def move_up():
    self.heading(90)
    self.forward(20)


def move_down():
    self.heading(270)
    self.backward(20)
