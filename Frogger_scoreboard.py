from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.current_level = 1
        self.write_level()

    def write_level(self):
        self.goto(x=-290, y=260)
        self.write(f"Level: {self.current_level}", True, align="left", font=FONT)

    def level_up(self):
        self.clear()
        self.current_level += 1
        self.write_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", True, align="center", font=FONT)