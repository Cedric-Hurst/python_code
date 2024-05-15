import time
from turtle import Screen
from frogger_player import Player
from frogger_car_manager import CarManager
from frogger_scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Froggie")

player = Player()
scoreboard = Scoreboard()
car_list = []
for _ in range(25):
    car = CarManager()
    car_list.append(car)

screen.listen()
screen.onkeypress(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in car_list:
        car.move()
        if car.xcor() < -330:
            car.reset_car()
        if player.distance(car) < 20:
            game_is_on = False
        if player.ycor() > 280:
            scoreboard.level_up()
            for car2 in car_list:
                car2.speed_up()
            player.starting_position()

scoreboard.game_over()
screen.exitonclick()
