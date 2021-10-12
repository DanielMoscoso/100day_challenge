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
        self.back_to_start()

    def move_up(self):
        """
        This makes the turtle face up and then move.
        """
        self.setheading(90)
        self.forward(20)

    def move_down(self):
        """
        This makes the turtle face down and then move.
        """
        self.setheading(270)
        self.forward(20)

    def back_to_start(self):
        self.goto(0, -280)
