import colorgram
import random
import turtle


# TODO: 1.- 10x10 matrix of dots.
# TODO: 2.- Every dot with a diameter of 20.
# TODO: 3.- Every dot with a space of 50 in between.

# ---------------------------- In case you need it ----------------------------
def reset_kernel():
    import os
    # os.getcwd()
    os.chdir('C:\\Users\\Daniel\\Documents\\Python\\100days\\Day_18\\hirst_painting')
# ---------------------------- In case you need it ----------------------------


def color_extraction(number_of_colors=0):
    colors = colorgram.extract('spot_paint.gif', number_of_colors)

    list_of_colors = []
    for color in colors:
        list_of_colors.append(tuple(color.rgb))

    return list_of_colors


def paint_matrix(turtle, color_list=[(0, 0, 0)], horizontal_dots=1, vertical_dots=1, starting_x=0):
    for _ in range(vertical_dots):  # Y axis
        move_sideways(turtle, color_list, horizontal_dots)

        turtle.penup()
        turtle.setposition(starting_x, turtle.position()[1] + 70)  # Up
        turtle.pendown()


def move_sideways(turtle, color_list, horizontal_dots):
    for _ in range(horizontal_dots):  # X axis
        color_choice = random.choice(color_list)
        turtle.color(color_choice)
        turtle.begin_fill()
        turtle.circle(20)
        turtle.end_fill()
        turtle.penup()
        turtle.setx(turtle.position()[0] + 70)  # Right
        turtle.pendown()


def set_up(turtle, starting_x=0, starting_y=0):
    tim.shape("turtle")
    tim.penup()
    tim.setposition(starting_x, starting_y)
    tim.pendown()


reset_kernel()

color_extraction(40)

color_list = [(246, 241, 244), (222, 152, 103), (233, 237, 240), (128, 172, 199),
              (221, 130, 149), (221, 73, 90), (243, 208, 99), (17, 121, 157),
              (118, 176, 147), (34, 120, 82), (18, 165, 204), (230, 74, 70),
              (142, 86, 60), (116, 85, 102), (162, 209, 162), (13, 169, 120),
              (171, 183, 219), (177, 154, 75), (213, 222, 213), (1, 98, 119),
              (54, 61, 96), (240, 177, 165), (221, 167, 185), (146, 204, 228), (24, 98, 61)]

starting_x = -400
starting_y = -350
horizontal_dots = int(input("How many horizontal dots: "))
vertical_dots = int(input("How many vertical dots: "))

turtle.colormode(255)

tim = turtle.Turtle()
set_up(tim, starting_x, starting_y)

paint_matrix(tim, color_list, horizontal_dots, vertical_dots, starting_x)

screen = turtle.Screen()
screen.exitonclick()
