from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

starting_position = [(0, 0), (-20, 0), (-40, 0)]

segments = []
for position in starting_position:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.setpos(position)
    segments.append(new_segment)


screen.exitonclick()
