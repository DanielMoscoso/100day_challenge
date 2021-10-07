from turtle import Turtle
import random

SPEED = 20


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
        self.ball.setheading(self.bouncing_direction(direction))

    def bouncing_direction(self, direction):
        up_left = random.randint(120, 150)
        up_right = random.randint(30, 60)
        down_left = random.randint(210, 240)
        down_right = random.randint(300, 330)

        if direction == "left" and self.ball.ycor() > 0:
            print("right wall")
            return up_left
        elif direction == "left" and self.ball.ycor() < 0:
            print("right wall")
            return down_left

        elif direction == "right" and self.ball.ycor() > 0:
            print("left wall")
            return up_right
        elif direction == "right" and self.ball.ycor() < 0:
            print("left wall")
            return down_right

        elif direction == "down" and self.ball.heading() < 90:
            print(f"Hit wall! facing: {self.ball.heading()}. going down_right: {down_right}")
            return down_right
        elif direction == "down" and self.ball.heading() > 90:
            print(f"Hit wall! facing: {self.ball.heading()}. going down_left: {down_left}")
            return down_left

        elif direction == "up" and self.ball.heading() < 270:
            return up_left
        elif direction == "up" and self.ball.heading() > 270:
            return up_right

    def move(self):
        self.ball.forward(SPEED)

    def x_cor(self):
        return self.ball.xcor()

    def y_cor(self):
        return self.ball.ycor()
