from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score_position()
        self.speed(0)  # Fastest
        self.write_score()

    def score_position(self):
        """
        This sets the position of the scoreboard for the given player.
        """
        if self.player == "one":
            self.goto(-200, 275)
        else:
            self.goto(200, 275)

    def write_score(self):
        """
        This writes the current score of the given player.
        """
        self.write(f"Score {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """
        This increases the the current score of the given player by 1.
        """
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        """
        This prints 'GAME OVER' on the middle of the screen.
        """
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=("Courier", 30, "normal"))
