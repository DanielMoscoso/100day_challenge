from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.speed(0)  # Fastest
        self.highscore = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.write_score()

    def reset(self):
        """
        It takes the score of the current game, and checks it if it is higher
        than the previous higher score. If it is, then updates the high score.
        """
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0

        self.write_score()
