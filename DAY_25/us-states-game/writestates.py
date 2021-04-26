from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class WriteStates(Turtle):

    def __init__(self, x_cord, y_cord, state_name):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(x_cord, y_cord)
        self.write(state_name)
