from turtle import Turtle


class Ball:
    def __init__(self):
        self.color = "white"
        self.shape = "square"
        self.size = 0.5
        self.add_ball()

    def add_ball(self):
        self.ball = Turtle(self.shape)
        self.ball.color = self.ball.color(self.color)
        self.ball.shapesize(self.size, self.size)
        self.ball.penup()
        self.ball.speed(0)
