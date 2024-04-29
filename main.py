from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def run_game():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)

    game_is_running = True
    while game_is_running:
        screen.update()
        time.sleep(0.1)
        snake.move()
        game_is_running = snake.out_of_bounds()

        if food.distance(snake.head) <= 15:
            snake.add_segment()
            food.new_position()
            scoreboard.add_score()

        for segments in snake.full_snake[1:]:
            if snake.head.distance(segments) < 10:
                game_is_running = False

    scoreboard.game_over()
    play_again = screen.textinput(title="Replay?", prompt="Do you want to play again? type y or n").lower()
    if play_again == 'y':
        screen.reset()
        run_game()
    else:
        screen.bye()


run_game()
