from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 14, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.speed(0)  # Fastest
        self.hideturtle()
        self.penup()
        self.goto(-200, 275)
        self.write_score()

    def write_score(self):
        """
        This writes the current level.
        """
        self.write(f"Score {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """
        This increases the the current level by 1.
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
