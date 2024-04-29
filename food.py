import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        random_position_x = random.randint(-250, 250)
        random_position_y = random.randint(-250, 250)
        self.goto(x=random_position_x, y=random_position_y)

    def new_position(self):
        random_position_x = random.randint(-250, 250)
        random_position_y = random.randint(-250, 250)
        self.goto(x=random_position_x, y=random_position_y)
