# TODO: 1.-Line in the middle of the screen.
# TODO: 2.-Individual class for the ball.
# TODO: 3.-Detect ball collision with walls.
# TODO: 4.-Individual class for the players.
# TODO: 5.-Detect ball collision with players for scores.
# TODO: 6.-Individual class for scores.

from turtle import Screen
from modules import ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

ball = ball.Ball()
screen.update()

screen.exitonclick()
