import turtle
from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
        print("up")

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
        print("down")

    # def create_paddle(self):
    #     # for position in POSITIONS:
    #     #     self.add_segment(position)
    #     self.paddle = Turtle(shape="square")
    #     self.paddle.color("white")
    #     self.paddle.penup()
    #     self.paddle.shapesize(stretch_wid=5, stretch_len=1)
    #     self.paddle.goto(350, 0)
    #

    # def add_segment(self, position):
    #     new_segment = Turtle(shape="square")
    #     new_segment.color("white")
    #     new_segment.penup()
    #     new_segment.goto(position)
    #     self.segments.append(new_segment)
    #
    # def move_up(self):
    #     for seg_num in range(len(self.segments) - 1, 0, -1):
    #         new_x = self.segments[seg_num - 1].xcor()
    #         new_y = self.segments[seg_num - 1].ycor()
    #         self.segments[seg_num].goto(new_x, new_y)
    #     self.segments[0].setheading(90)
    #     self.segments[0].forward(MOVE_DISTANCE)
    #
