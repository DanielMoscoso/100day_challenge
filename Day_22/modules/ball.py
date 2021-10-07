from turtle import Turtle
import random

VELOCITY = 20


class Ball:
    def __init__(self):
        self.color = "white"
        self.shape = "square"
        self.size = 0.5
        self.add_ball()

    def add_ball(self):
        self.ball = Turtle(self.shape)
        self.ball.color(self.color)
        self.ball.shapesize(self.size, self.size)
        self.ball.penup()
        self.ball.setpos((0, -1))
        self.ball.speed(0)

    def bounce(self, direction):
        up_left = random.randint(120, 150)
        up_right = random.randint(30, 60)
        down_left = random.randint(210, 240)
        down_right = random.randint(300, 330)

        if direction == "left" and self.ball.ycor() > 0:
            self.ball.setheading(up_left)
        elif direction == "left" and self.ball.ycor() < 0:
            self.ball.setheading(down_left)

        elif direction == "right" and self.ball.ycor() > 0:
            self.ball.setheading(up_right)
        elif direction == "right" and self.ball.ycor() < 0:
            self.ball.setheading(down_right)

        elif direction == "down" and self.ball.heading() < 90:
            self.ball.setheading(down_right)
        elif direction == "down" and self.ball.heading() > 90:
            self.ball.setheading(down_left)

        elif direction == "up" and self.ball.heading() < 270:
            self.ball.setheading(up_left)
        elif direction == "up" and self.ball.heading() > 270:
            self.ball.setheading(up_right)

    def move(self):
        self.ball.forward(VELOCITY)

    def x_cor(self):
        return self.ball.xcor()

    def y_cor(self):
        return self.ball.ycor()
