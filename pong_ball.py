from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 15
        self.y_move = 15
        self.move_speed = 0.1

    def set_ball(self):
        self.goto(0, 0)
        self.move_speed = 0.1

    def move(self):
        top_bound = (self.xcor(), 280)
        bottom_bound = (self.xcor(), -280)
        self.floor_bounce(top_bound, bottom_bound)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def floor_bounce(self, top_bound, bottom_bound):
        if self.distance(top_bound) < 20:
            self.y_move *= -1
        elif self.distance(bottom_bound) < 20:
            self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9
