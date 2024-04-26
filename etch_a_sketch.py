from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move():
    t.fd(10)


def left():
    t.left(10)


def right():
    t.right(10)


def back():
    t.back(10)


def clear():
    t.clear()
    t.teleport(x=0, y=0)
    t.setheading(0)


screen.listen()
screen.onkey(fun=move, key='w')
screen.onkey(fun=left, key='a')
screen.onkey(fun=right, key='d')
screen.onkey(fun=back, key='s')
screen.onkey(fun=clear, key='c')
screen.exitonclick()
