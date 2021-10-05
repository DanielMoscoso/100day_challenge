from turtle import Turtle
# # ---------------------------- In case you need it ----------------------------
# def reset_kernel():
#     """
#     This function helps set up the kernel location. Just in case the IDE is running
#     in a different location.
#     """
#     import os
#     os.getcwd()
#     os.chdir('C:\\Users\\Daniel\\Documents\\Python\\100days\\Day_20\\modules')
# # ---------------------------- In case you need it ----------------------------

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.setpos(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        # If you are facing down, then do not go over youself.
        if self.segments[0].heading() == 270:
            pass
        else:
            self.segments[0].setheading(90)

    def left(self):
        # If you are facing left, then do not go over youself.
        if self.segments[0].heading() == 0:
            pass
        else:
            self.segments[0].setheading(180)

    def down(self):
        # If you are facing up, then do not go over youself.
        if self.segments[0].heading() == 90:
            pass
        else:
            self.segments[0].setheading(270)

    def right(self):
        # If you are facing left, then do not go over youself.
        if self.segments[0].heading() == 180:
            pass
        else:
            self.segments[0].setheading(0)
