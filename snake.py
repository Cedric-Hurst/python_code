from turtle import Turtle

MOVE_DISTANCE = 20
POS_BOUND = 280
NEG_BOUND = -280
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_size = 3
        self.full_snake = []
        self.create_snake()
        self.head = self.full_snake[0]

    def create_snake(self):
        for body in range(self.snake_size):
            snake_segment = Turtle(shape="square")
            snake_segment.penup()
            snake_segment.color("white")
            snake_segment.goto(x=body * -20, y=0)
            self.full_snake.append(snake_segment)

    def move(self):
        for seg_num in range(len(self.full_snake) - 1, 0, -1):
            position = self.full_snake[seg_num - 1].position()
            self.full_snake[seg_num].goto(x=position[0], y=position[1])
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def out_of_bounds(self):
        if self.head.xcor() > POS_BOUND or self.head.xcor() < NEG_BOUND:
            return False
        elif self.head.ycor() > POS_BOUND or self.head.ycor() < NEG_BOUND:
            return False
        else:
            return True

    def add_segment(self):
        self.snake_size += 1
        snake_segment = Turtle(shape="square")
        snake_segment.penup()
        snake_segment.color("white")
        position = self.full_snake[-1].position()
        snake_segment.goto(x=position[0], y=position[1])
        self.full_snake.append(snake_segment)

