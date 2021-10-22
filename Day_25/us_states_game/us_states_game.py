# TODO: 1.-Convert the guess into a title case.
# TODO: 2.-Check if the guess is among the 50 states.
# TODO: 3.-Write correct guesses onto the map.
# TODO: 4.-Use a loop to allow the user to keep guessing.
# TODO: 5.-Record the correct guesses in a list.
# TODO: 6.-Keep track of the score.

import turtle
import os
import pandas as pd
from modules import pin

# os.getcwd()
# os.chdir("./Day_25/us_states_game")


# # In case you need to see the 'X' and 'Y' coordinates:
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
def coordinates(state):
    """
    This will return the 'x' and 'y' coordinates for the given state as a tuple.
    """
    x = int(raw_data[raw_data["state"] == state].x)
    y = int(raw_data[raw_data["state"] == state].y)

    return (x, y)


raw_data = pd.read_csv("50_states.csv")
missed_states = pd.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(750, 520)

image = "blank_states_img.gif"
screen.addshape(image)
pin = pin.Pin()
turtle.shape(image)

answer_state = screen.textinput("Guess the state", "What is another state's name?").title()

guessed_states = set()
counter = 50
while len(guessed_states) < 50 and counter > 0:
    if answer_state == "Exit":
        break
    elif answer_state not in raw_data["state"].to_list():
        counter -= 1
    else:
        guessed_states.add(answer_state)
        pin.go_location(answer_state, coordinates(answer_state))

    answer_state = screen.textinput(f"{counter}/50", "What is another state's name?").title()
    # if counter == 0:
    #     pass
    # else:
    #     answer_state = screen.textinput(f"{counter}/50", "What is another state's name?").title()

for state in guessed_states:
    missed_states = missed_states.drop(raw_data[raw_data["state"] == state].index)

missed_states.to_csv("missed_states.csv", columns=["state"], header=False, index=False)

screen.exitonclick()
