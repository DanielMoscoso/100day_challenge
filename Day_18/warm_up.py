from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")

# # Rectangle:
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

# Dotted line:
for i in range(20):
    tim.forward(5)
    tim.penup()
    tim.forward(5)
    tim.pendown()


screen = Screen()
screen.exitonclick()
