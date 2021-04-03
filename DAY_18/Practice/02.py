from turtle import Turtle, Screen

trix = Turtle()

trix.shape("turtle")
trix.color("red")
for _ in range(15):
    trix.forward(10)
    trix.penup()
    trix.forward(10)
    trix.pendown()

screen = Screen()
screen.exitonclick()
