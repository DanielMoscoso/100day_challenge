# TODO: 1.-Line in the middle of the screen.
# TODO: 2.-Individual class for the ball.
# TODO: 3.-Detect ball collision with walls.
# TODO: 4.-Individual class for the players.
# TODO: 5.-Detect ball collision with players for scores.
# TODO: 6.-Individual class for scores.

from turtle import Turtle, Screen
from modules import ball, middle_line
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

middle_line.Middle_Line()

pong_ball = ball.Ball()
while True:
    screen.update()
    time.sleep(0.1)

    # If it hits a wall, game over:
    if pong_ball.x_cor() > 370:  # Right wall
        pong_ball.bounce("left")
    elif pong_ball.x_cor() < -370:  # Left wall
        pong_ball.bounce("right")
    elif pong_ball.y_cor() > 270:  # Upper wall
        pong_ball.bounce("down")
    elif pong_ball.y_cor() < -270:  # Lower wall
        pong_ball.bounce("up")

    pong_ball.move()

screen.exitonclick()
