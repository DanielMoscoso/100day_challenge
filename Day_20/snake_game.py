from turtle import Screen
import time
from modules import snake
from modules import food
from modules import scoreboard
# # ---------------------------- In case you need it ----------------------------
# def reset_kernel():
#     """
#     This function helps set up the kernel location. Just in case the IDE is running
#     in a different location.
#     """
#     import os
#     os.getcwd()
#     os.chdir('C:\\Users\\Daniel\\Documents\\Python\\100days\\Day_20\\modules')
# # ---------------------------- In case you need it ----------------------------

# TODO: 1.-Create a snake body.
# TODO: 2.-Move the snake.
# TODO: 3.-Control the snake.
# TODO: 4.-Detect collision with food.
# TODO: 5.-Create a scoreboard.
# TODO: 6.-Detect collision with wall.
# TODO: 7.-Detect collision with tail.

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = snake.Snake()
food = food.Food()
score = scoreboard.Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Eating a dot:
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # If it hits a wall, game over:
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # If it eats itself, game over:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
