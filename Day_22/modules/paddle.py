from turtle import Turtle

STARTING_POSITION = [[(-300, -40), (-300, -20), (-300, 0), (-300, 20), (-300, 40)],
                     [(300, -40), (300, -20), (300, 0), (300, 20), (300, 40)]]
SHAPE = "square"
COLOR = "white"
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Paddle:
    def __init__(self, player):
        self.player = player
        self.segments = []
        self.create_paddle()

    def create_paddle(self):
        if self.player == "one":
            for position in STARTING_POSITION[0]:
                self.add_segment(position)
        else:
            for position in STARTING_POSITION[1]:
                self.add_segment(position)
        print(self.segments)

    def add_segment(self, position):
        new_segment = Turtle(SHAPE)
        new_segment.color(COLOR)
        new_segment.penup()
        new_segment.setpos(position)
        new_segment.speed(0)
        self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # If you are facing down, then do not go over youself.
        if self.head.heading() == DOWN:
            pass
        else:
            self.head.setheading(UP)

    def left(self):
        # If you are facing left, then do not go over youself.
        if self.head.heading() == RIGHT:
            pass
        else:
            self.head.setheading(LEFT)

    def down(self):
        # If you are facing up, then do not go over youself.
        if self.head.heading() == UP:
            pass
        else:
            self.head.setheading(DOWN)

    def right(self):
        # If you are facing left, then do not go over youself.
        if self.head.heading() == LEFT:
            pass
        else:
            self.head.setheading(RIGHT)
