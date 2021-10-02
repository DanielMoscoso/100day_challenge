import colorgram
from turtle import Turtle, Screen
import random


# TODO: 1.- 10x10 matrix of dots.
# TODO: 2.- Every dot with a diameter of 20.
# TODO: 3.- Every dot with a space of 50 in between.

# # ---------------------------- In case you need it ----------------------------
# def reset_kernel():
#     import os
#     # os.getcwd()
#     os.chdir('C:\\Users\\Daniel\\Documents\\Python\\100days\\Day_18\\hirst_painting')
# # ---------------------------- In case you need it ----------------------------


def color_extraction(number_of_colors=0):
    colors = colorgram.extract('spot_paint.gif', number_of_colors)

    list_of_colors = []
    for color in colors:
        list_of_colors.append(tuple(color.rgb))

    return list_of_colors


color_extraction(40)

# %%
color_list = [(246, 241, 244), (222, 152, 103), (233, 237, 240), (128, 172, 199),
              (221, 130, 149), (221, 73, 90), (243, 208, 99), (17, 121, 157),
              (118, 176, 147), (34, 120, 82), (18, 165, 204), (230, 74, 70),
              (142, 86, 60), (116, 85, 102), (162, 209, 162), (13, 169, 120),
              (171, 183, 219), (177, 154, 75), (213, 222, 213), (1, 98, 119),
              (54, 61, 96), (240, 177, 165), (221, 167, 185), (146, 204, 228), (24, 98, 61)]

import turtle
import random
turtle.colormode(255)
tim = turtle.Turtle()
tim.shape("turtle")
tim.penup()
tim.setposition(-400, -350)
tim.pendown()

# Dotted line:
for i in range(10):
    color_choice = random.choice(color_list)
    tim.color(color_choice)
    tim.begin_fill()
    tim.circle(20)
    tim.end_fill()
    tim.penup()
    tim.setx(tim.position()[0] + 70)
    tim.pendown()

screen = turtle.Screen()
screen.exitonclick()
