from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Courier", 8, "normal")


class Pin(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(0)

    def go_location(self, name, location):
        self.goto(location)
        self.write(f"{name}", align=ALIGNMENT, font=FONT)
