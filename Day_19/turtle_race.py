from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter color:  ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

# Object creation:
token = -100
for number, item in enumerate(colors):
    turtles.append(Turtle(shape="turtle"))
    turtles[number].color(item)
    turtles[number].penup()
    turtles[number].goto(x=-230, y=token)
    turtles[number].speed(0)
    token += 40

move = True
while move:
    for number in range(6):
        turtles[number].forward(random.randint(0, 10))

        if turtles[number].xcor() > 230:
            move = False
            if user_bet == colors[number]:
                print(f"You win!!. The {colors[number]} turtle is the winner!")
            else:
                print(f"You lose. The {colors[number]} turtle is the winner.")
