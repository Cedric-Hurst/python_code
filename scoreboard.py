from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 15, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.current_score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.current_score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 50)
        self.write(arg=f"Game Over.", align=ALIGNMENT, font=FONT)
