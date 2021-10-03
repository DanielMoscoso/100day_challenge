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


# # --------------------------------- 7 shapes: ---------------------------------
# def draw_shape(shape):
#     angle = 360 / shape
#
#     for vertices in range(shape):
#         tim.forward(110)
#         tim.right(angle)
#
#     # # This is if you want a completely random color:
#     # color1 = round(random.randint(0, 100) * 0.01, 2)  # From 0 to 1
#     # color2 = round(random.randint(0, 100) * 0.01, 2)  # From 0 to 1
#     # color3 = round(random.randint(0, 100) * 0.01, 2)  # From 0 to 1
#     # tim.pencolor((color1, color2, color3))
#
#     # # This is if you want a set of colors:
#     colors = ['cyan', 'blue', 'lime', 'magenta', 'tomato', 'sienna', 'teal', 'light slate gray', 'light coral', 'wheat']
#     tim.color(random.choice(colors))
#
#
# vertices_list = [3, 4, 5, 6, 7, 8, 9, 10]
# for shape in vertices_list:
#     draw_shape(shape)
# # --------------------------------- 7 shapes: ---------------------------------


# # -------------------------- Completely Random Walk: --------------------------
# def random_walk():
#     tim.pensize(8)
#     tim.speed(0)
#     direction = [0, 90, 180, 270]
#
#     tim.forward(30)
#     tim.setheading(random.choice(direction))
#
#     # # This is if you want a completely random color:
#     # color1 = random.randint(0, 255))
#     # color2 = random.randint(0, 255))
#     # color3 = random.randint(0, 255))
#     # tim.pencolor((color1, color2, color3))
#
#     # # This is if you want a set of colors:
#     colors = ['cyan', 'SeaGreen', 'CornFlowerBlue', 'IndianRed', 'DarkOrchid', 'LightSeaGreen', 'teal', 'slate gray', 'light coral', 'wheat']
#     tim.color(random.choice(colors))
#
#
# for _ in range(200):
#     random_walk()
# # -------------------------- Completely Random Walk: --------------------------


# # -------------------------------- Spirograph: --------------------------------
# def Spirograph():
#     tim.pensize(1)
#     tim.speed(0)
#     direction = [0, 90, 180, 270]
#
#     tim.circle(200)
#
#     # # This is if you want a completely random color:
#     # color1 = random.randint(0, 255))
#     # color2 = random.randint(0, 255))
#     # color3 = random.randint(0, 255))
#     # tim.pencolor((color1, color2, color3))
#
#     # # This is if you want a set of colors:
#     colors = ['cyan', 'SeaGreen', 'CornFlowerBlue', 'IndianRed', 'DarkOrchid', 'LightSeaGreen', 'teal', 'slate gray', 'light coral', 'wheat']
#     tim.color(random.choice(colors))
#     tim.right(3)
#
#
# for _ in range(120):
#     Spirograph()
# # -------------------------------- Spirograph: --------------------------------


# ------------------------------ Spirograph 2.0: ------------------------------
def Spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):  # '//' means floor division. Normal division would output a float.
        tim.pensize(1)
        tim.speed(0)

        tim.circle(200)

        # # This is if you want a completely random color:
        # color1 = random.randint(0, 255))
        # color2 = random.randint(0, 255))
        # color3 = random.randint(0, 255))
        # tim.pencolor((color1, color2, color3))

        # # This is if you want a set of colors:
        colors = ['cyan', 'SeaGreen', 'CornFlowerBlue', 'IndianRed', 'DarkOrchid', 'LightSeaGreen', 'teal', 'slate gray', 'light coral', 'wheat']
        tim.color(random.choice(colors))
        tim.setheading(tim.heading() + size_of_gap)  # This is to also turn right.


Spirograph(5)  # 5 degree ofset from circle to circle.
# ------------------------------ Spirograph 2.0: ------------------------------

screen = Screen()
screen.exitonclick()
