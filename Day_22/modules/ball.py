from turtle import Turtle
import random

DISTANCE = 20


class Ball:
    def __init__(self):
        self.color = "white"
        self.shape = "circle"
        self.size = 0.5
        self.ball = self.add_ball()

    def add_ball(self):
        """
        Here a turtle object is created, and then turned into a ball.
        """
        ball = Turtle(self.shape)
        ball.color(self.color)
        ball.shapesize(self.size, self.size)
        ball.penup()
        ball.setpos((0, -1))
        ball.speed(0)

        return ball

    def bounce(self, direction):
        """
        Here is the logic for the bouncing. The direction can be 'left' or 'right'.
        Then it calculates the bouncing angle with the 'bouncing_direction()', and
        points the ball towards that angle.
        """
        self.ball.setheading(self.bouncing_direction(direction))
        # The ball needs to move a little more every time it hits a wall.
        # Otherwise, it gets confused on very tight edges.
        self.ball.forward(5)

    def bouncing_direction(self, direction):
        """
        This calculates and returnd the angle for the bouncing. The direction is
        being taken in as a parameter.
        """
        up_left = random.randint(120, 150)
        up_right = random.randint(30, 60)
        down_left = random.randint(210, 240)
        down_right = random.randint(300, 330)

        if direction == "left" and self.ball.ycor() > 0:
            return up_left
        elif direction == "left" and self.ball.ycor() < 0:
            return down_left

        elif direction == "right" and self.ball.ycor() > 0:
            return up_right
        elif direction == "right" and self.ball.ycor() < 0:
            return down_right

        elif direction == "down" and self.ball.heading() < 90:
            return down_right
        elif direction == "down" and self.ball.heading() > 90:
            return down_left

        elif direction == "up" and self.ball.heading() < 270:
            return up_left
        elif direction == "up" and self.ball.heading() > 270:
            return up_right

    def move(self):
        """
        Makes the ball move a certain number of units.
        """
        self.ball.forward(DISTANCE)

    def reset_pos(self):
        """
        It resets the position of the ball to the origin, and sets the direction
        pointing toward the right.
        """
        self.ball.setpos((0, 0))
        self.ball.setheading(0)

    def x_cor(self):
        """
        It gives the 'X' coordinates of the ball.
        """
        return self.ball.xcor()

    def y_cor(self):
        """
        It gives the 'Y' coordinates of the ball.
        """
        return self.ball.ycor()
