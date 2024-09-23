from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
STEP_SIZE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.snake_body = list()
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for pos in START_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, pos):
        if pos == START_POSITIONS[0]:
            body = Turtle(shape="circle")
            body.color("yellow")
        else:
            body = Turtle(shape="square")
            body.color("pink")
        body.penup()
        body.setpos(pos)
        self.snake_body.append(body)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for part_position in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[part_position - 1].xcor()
            new_y = self.snake_body[part_position - 1].ycor()
            self.snake_body[part_position].setpos(new_x, new_y)
        self.head.fd(STEP_SIZE)

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

    # def reset(self):
    #     for seg in self.snake_body:
    #         seg.hideturtle()
    #     self.snake_body.clear()
    #     self.create_snake()
    #     self.head = self.snake_body[0]
