from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')


class Scoreboard(Turtle):

    def __init__(self, player):
        super().__init__()
        self.current_score = 0
        self.shape("square")
        self.color("white")
        self.hideturtle()
        self.penup()
        if player == "player":
            self.goto(x=-100, y=250)
        elif player == "opponent":
            self.goto(x=70, y=250)
        self.draw_scores = [self.draw_0, self.draw_1, self.draw_2, self.draw_3]
        self.update_scoreboard()

    def update_scoreboard(self):
        self.draw_scores[self.current_score]()

    def add_score(self):
        self.current_score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self, player):
        self.goto(0, 50)
        self.write(arg=f"Game Over. {player} is the winner!", align=ALIGNMENT, font=FONT)

    def draw_0(self):
        self.setheading(90)
        self.shapesize(stretch_wid=.5, stretch_len=3)
        self.stamp()
        self.setheading(0)
        self.forward(35)
        self.setheading(90)
        self.stamp()
        self.forward(25)
        self.setheading(180)
        self.forward(15)
        self.shapesize(stretch_wid=.5, stretch_len=1.5)
        self.stamp()
        self.setheading(270)
        self.forward(50)
        self.setheading(180)
        self.stamp()

    def draw_1(self):
        self.setheading(90)
        self.forward(25)
        self.shapesize(stretch_wid=.5, stretch_len=3)
        self.stamp()

    def draw_2(self):
        self.setheading(90)
        self.forward(25)
        self.setheading(0)
        self.shapesize(stretch_wid=.5, stretch_len=2)
        self.stamp()

        self.forward(15)
        self.setheading(270)
        self.forward(10)
        self.shapesize(stretch_wid=.5, stretch_len=1.25)
        self.stamp()

        self.forward(15)
        self.setheading(180)
        self.forward(15)
        self.shapesize(stretch_wid=.5, stretch_len=2)
        self.stamp()

        self.forward(15)
        self.setheading(270)
        self.forward(10)
        self.shapesize(stretch_wid=.5, stretch_len=1.25)
        self.stamp()

        self.forward(15)
        self.setheading(0)
        self.forward(15)
        self.shapesize(stretch_wid=.5, stretch_len=2)
        self.stamp()

    def draw_3(self):
        self.forward(15)
        self.setheading(90)
        self.forward(25)
        self.shapesize(stretch_wid=.5, stretch_len=3)
        self.stamp()

        self.forward(25)
        self.setheading(180)
        self.forward(20)
        self.shapesize(stretch_wid=.5, stretch_len=1.5)
        self.stamp()

        self.setheading(270)
        self.forward(25)
        self.setheading(180)
        self.stamp()

        self.setheading(270)
        self.forward(25)
        self.setheading(180)
        self.stamp()
