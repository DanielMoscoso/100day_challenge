from turtle import Turtle

SHAPE = "square"
COLOR = "white"
SIZE = 0.5


class Middle_Line:
    def __init__(self):
        self.add_marker()

    def add_marker(self):
        timmy = Turtle(SHAPE)
        timmy.color(COLOR)
        timmy.shapesize(SIZE, SIZE)
        timmy.penup()
        timmy.setpos((0, -290))
        timmy.setheading(90)
        timmy.speed(0)

        self.create_lines(timmy)

    def create_lines(self, turtle):
        for _ in range(0, 600, 20):
            turtle.pendown()
            turtle.forward(10)
            turtle.penup()
            turtle.forward(10)
