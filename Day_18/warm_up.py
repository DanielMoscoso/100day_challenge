from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("red")

# # Rectangle:
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

# # Dotted line:
# for i in range(20):
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()


# 7 shapes:
def draw_shape(shape):
    angle = 360 / shape

    for vertices in range(shape):
        tim.forward(110)
        tim.right(angle)

    # # This is if you want a completely random color:
    # color1 = round(random.randint(0, 100) * 0.01, 2)
    # color2 = round(random.randint(0, 100) * 0.01, 2)
    # color3 = round(random.randint(0, 100) * 0.01, 2)
    # tim.pencolor((color1, color2, color3))

    # # This is if you want a set of colors:
    # colors = ['cyan', 'blue', 'lime', 'magenta', 'tomato', 'sienna', 'teal', 'light slate gray', 'light coral']
    # tim.color(random.choice(colors))


vertices_list = [3, 4, 5, 6, 7, 8, 9, 10]
for shape in vertices_list:
    draw_shape(shape)

screen = Screen()
screen.exitonclick()
