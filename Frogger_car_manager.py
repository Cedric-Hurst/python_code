from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.move_distance = STARTING_MOVE_DISTANCE
        self.make_car()
        self.starting_x_rang = random.randrange(-300, 350, random.randrange(1, 25))
        self.y_rang = random.randrange(-220, 260, random.randrange(1, 25))
        self.restart_x_rang = random.randrange(330, 350, random.randrange(1, 25))

        self.goto(x=self.starting_x_rang, y=self.y_rang)

    def move(self):
        self.goto(x=self.xcor()-self.move_distance, y=self.ycor())

    def make_car(self):
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()

    def reset_car(self):
        self.clear()
        self.make_car()
        self.goto(x=self.restart_x_rang, y=self.y_rang)

    def speed_up(self):
        self.move_distance += MOVE_INCREMENT
