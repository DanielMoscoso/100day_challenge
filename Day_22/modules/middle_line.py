from turtle import Turtle


class Middle_Line:
    def __init__(self):
        self.color = "white"
        self.shape = "square"
        self.size = 0.5
        self.add_marker()

    def add_marker(self):
        timmy = Turtle(self.shape)
        timmy.color(self.color)
        timmy.shapesize(self.size, self.size)
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
