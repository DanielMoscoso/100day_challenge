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
# os.chdir("./Day_25")

screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(750, 520)

image = "blank_states_img.gif"
screen.addshape(image)
pin = pin.Pin()
turtle.shape(image)


# # In case you need to see the 'X' and 'Y' coordinates:
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

answer_state = screen.textinput("Guess the state", "What is another state's name?").title()

raw_data = pd.read_csv("50_states.csv")

pin.go_location((100, 100), answer_state)


screen.exitonclick()
