# TODO: 1.-Line in the middle of the screen.
# TODO: 2.-Individual class for the ball.
# TODO: 2.1.-Ball movement.
# TODO: 3.-Individual class for scores.
# TODO: 4.-Individual class for the players' paddles.
# TODO: 4.1.-Paddle movement.
# TODO: 5.-Detect ball collision with players' paddles.
# TODO: 6.-Detect ball collision with lateral walls for scores.

from turtle import Turtle, Screen
from modules import ball, middle_line, scoreboard, paddle
import time


def new_game():
    pong_ball.reset_pos()
    paddle_one.reset_paddle()
    paddle_two.reset_paddle()
    screen.update()


def paddle_bounce(paddle):
    if paddle.player == "one":
        for segment in paddle.segments:
            if pong_ball.ball.distance(segment) < 21:
                pong_ball.bounce("right")
    else:
        for segment in paddle.segments:
            if pong_ball.ball.distance(segment) < 21:
                pong_ball.bounce("left")


def wall_bouncing():
    if pong_ball.y_cor() > 270:  # Upper wall
        pong_ball.bounce("down")
    elif pong_ball.y_cor() < -270:  # Lower wall
        pong_ball.bounce("up")
    else:  # Anithing in between
        pass


def play(repeat=True, lives=5):
    if pong_ball.x_cor() > 340:
        player_one.increase_score()
        new_game()
        if player_one.score == lives:
            player_two.game_over()
            repeat = False
        time.sleep(0.6)
    elif pong_ball.x_cor() < -340:
        player_two.increase_score()
        new_game()
        if player_two.score == lives:
            player_one.game_over()
            repeat = False
        time.sleep(0.6)
    else:
        pass

    return repeat


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

middle_line.Middle_Line()

player_one = scoreboard.Scoreboard("one")
player_two = scoreboard.Scoreboard("two")
paddle_one = paddle.Paddle("one")
paddle_two = paddle.Paddle("two")

screen.listen()
screen.onkey(paddle_one.up, "w")
screen.onkey(paddle_one.down, "s")

screen.onkey(paddle_two.up, "o")
screen.onkey(paddle_two.down, "l")

pong_ball = ball.Ball()

while play():
    screen.update()
    time.sleep(0.1)

    pong_ball.move()

    # If it hits the upper or lower wall, then bounce:
    wall_bouncing()

    # Bounce off player one's paddle:
    paddle_bounce(paddle_one)
    # Bounce off player two's paddle:
    paddle_bounce(paddle_two)

screen.exitonclick()
