from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, player_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(player_position)

    def move_up(self):
        if self.ycor() < 270:
            self.goto(x=self.xcor(), y=self.ycor()+30)

    def move_down(self):
        if self.ycor() > -250:
            self.goto(x=self.xcor(), y=self.ycor()-30)

    def auto_move(self):
        if self.distance(x=350, y=270) < 20:
            self.goto(x=self.xcor(), y=self.ycor()+30)
        elif self.distance(x=350, y=-270) < 20:
            self.goto(x=self.xcor(), y=self.ycor()-30)