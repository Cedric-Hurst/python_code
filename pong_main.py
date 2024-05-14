from turtle import Turtle, Screen
import time
from pong_paddle import Paddle
from pong_scoreboard import Scoreboard
from pong_ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


player_scoreboard = Scoreboard("player")
opponent_scoreboard = Scoreboard("opponent")

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

ball = Ball()

screen.listen()

screen.onkeypress(key="Up", fun=right_paddle.move_up)
screen.onkeypress(key="Down", fun=right_paddle.move_down)
screen.onkeypress(key="w", fun=left_paddle.move_up)
screen.onkeypress(key="s", fun=left_paddle.move_down)

game_is_running = True
while game_is_running:

    screen.update()
    time.sleep(ball.move_speed)
    #right_paddle.auto_move()
    ball.move()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -320 or ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.paddle_bounce()

    if ball.distance(x=390, y=ball.ycor()) < 10:
        player_scoreboard.add_score()
        ball.set_ball()
    elif ball.distance(x=-390, y=ball.ycor()) < 10:
        opponent_scoreboard.add_score()
        ball.set_ball()

    if player_scoreboard.current_score == 3:
        player_scoreboard.game_over("Player")
        game_is_running = False
    elif opponent_scoreboard.current_score == 3:
        opponent_scoreboard.game_over("Opponent")
        game_is_running = False


screen.exitonclick()
