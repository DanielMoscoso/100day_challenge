from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def left_move():
    tim.left(5)
    tim.forward(10)


def right_move():
    tim.right(5)
    tim.forward(10)


def clear_all():
    tim.reset()
    tim.setheading(0)  # East.


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=left_move)
screen.onkey(key="d", fun=right_move)
screen.onkey(key="c", fun=clear_all)
screen.exitonclick()
