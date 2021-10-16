import turtle

screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(750, 520)

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

screen.exitonclick()
