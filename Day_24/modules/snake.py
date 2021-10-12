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
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """
        This creates the 3-segment-snake and places it on the starting position.
        (With its head on the center, facing east, and its tail facing west).
        """
        for position in STARTING_POSITION:
            self.add_segment(position)

    def extend(self):
        """
        This takes the position of the last segment/link and adds a new segment/link
        right behind it.
        """
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        """
        This takes the position as an argument, and uses it to create a segment/link,
        which is then placed in the position that was passed. This is done by appending
        a new objecto to the 'segments' list.
        """
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setpos(position)
        new_segment.speed(0)
        self.segments.append(new_segment)

    def reset(self):
        """
        It deletes all the segments previously obtained by the snake (deletes
        all the objects in the list), then creates a new snake from scratch and
        sets it up in the middle of the screen.
        """
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        """
        This first takes the location of the snake's head, then moves the trailing
        segment to the current head's location, repeating the process until reaching
        the last segment of the snake. Then it moves the head forward. (It behaves
        like a caterpilar).
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """
        This changes the snake's head direction to NORTH, if and only if, the snake is
        NOT currently facing SOUTH. This is to prevent the snake from trampling itself.
        """
        # If you are facing down, then do not go over youself.
        if self.head.heading() == DOWN:
            pass
        else:
            self.head.setheading(UP)

    def left(self):
        """
        This changes the snake's head direction to WEST, if and only if, the snake is
        NOT currently facing EAST. This is to prevent the snake from trampling itself.
        """
        # If you are facing left, then do not go over youself.
        if self.head.heading() == RIGHT:
            pass
        else:
            self.head.setheading(LEFT)

    def down(self):
        """
        This changes the snake's head direction to SOUTH, if and only if, the snake is
        NOT currently facing NORTH. This is to prevent the snake from trampling itself.
        """
        # If you are facing up, then do not go over youself.
        if self.head.heading() == UP:
            pass
        else:
            self.head.setheading(DOWN)

    def right(self):
        """
        This changes the snake's head direction to EAST, if and only if, the snake is
        not currently facing WEST. This is to prevent the snake from trampling itself.
        """
        # If you are facing left, then do not go over youself.
        if self.head.heading() == LEFT:
            pass
        else:
            self.head.setheading(RIGHT)
