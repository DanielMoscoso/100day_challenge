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
        """
        It creates the paddle shape from the 'STARTING_POSITION' list. Which has
        2 lists inside; one for the first player's paddle and the other for the
        second player's. The paddle consists of 4 turtle square objects, therefore,
        containing 4 bundle of X and Y coordinates.
        """
        if self.player == "one":
            for position in STARTING_POSITION[0]:
                self.add_segment(position)
        else:
            for position in STARTING_POSITION[1]:
                self.add_segment(position)

    def add_segment(self, position):
        """
        This adds a segment, or a link to the specific player's paddle. It takes
        the 'position' argument for player 1 or 2 depending on what the user needs.
        """
        new_segment = Turtle(SHAPE)
        new_segment.color(COLOR)
        new_segment.penup()
        new_segment.setpos(position)
        new_segment.speed(0)
        self.segments.append(new_segment)

    def reset_paddle(self):
        """
        This resets the position of the designated paddle.
        """
        if self.player == "one":
            for index, position in enumerate(STARTING_POSITION[0]):
                self.segments[index].goto(position)
        else:
            for index, position in enumerate(STARTING_POSITION[1]):
                self.segments[index].goto(position)

    def move_down(self):
        """
        It takes the list of objects that form the paddle in the order that were
        inserted. Then starts moving them DOWN, one by one. Since the paddle is
        moving DOWN, the FIRST ITEM on the list is the top of the paddle.
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        """
        It takes the list of objects that form the paddle in the order that were
        inserted. Then starts moving them UP, one by one. Since the paddle is
        moving UP, the FIRST ITEM on the list is now the bottom of the paddle.
        """
        for seg_num in range(0, len(self.segments) - 1):
            new_x = self.segments[seg_num + 1].xcor()
            new_y = self.segments[seg_num + 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """
        The head of the paddle is set to the LAST item added to the list of segments,
        in other word, the TOP of the paddle. Then sets the direction towards
        north, and moves UP.
        """
        self.head = self.segments[-1]
        self.head.setheading(UP)
        self.move_up()

    def down(self):
        """
        The head of the paddle is set to the FIRST item added to the list of segments,
        in other word, the BOTTOM of the paddle. Then sets the direction towards
        south, and moves DOWN.
        """
        self.head = self.segments[0]
        self.head.setheading(DOWN)
        self.move_down()
