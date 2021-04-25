import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.y_cord = random.randint(-250, 250)
        self.x_cord = 280
        self.car_speed = STARTING_MOVE_DISTANCE
        self.create_car()

    def create_car(self):
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(self.x_cord, self.y_cord)

    def move_car(self):
        new_x = self.xcor() - self.car_speed
        self.goto(new_x, self.ycor())
