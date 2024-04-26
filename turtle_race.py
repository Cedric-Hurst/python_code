from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_guess = screen.textinput(title="Place your bets!", prompt="Which turtle will win the race? Enter a color: ")
y = 125
is_race_on = False
colors = ["red", "blue", "orange", "yellow", "purple", "green"]
all_turtles = []
for index in range(0, 6):
    new_t = Turtle(shape="turtle")
    new_t.color(colors[index])
    new_t.teleport(x=-230, y=y)
    new_t.penup()
    y -= 50
    all_turtles.append(new_t)

if user_guess:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_guess:
                print(f"{winner} turtle has won the race! Congrats on picking the best turtle!")
            else:
                print(f"{winner} turtle has won the race! You did not pick the best turtle.")
            break


screen.exitonclick()
