from turtle import Turtle, Screen

trix = Turtle()

trix.shape("turtle")
trix.color("red")
for _ in range(4):
    trix.forward(100)
    trix.right(90)

screen = Screen()
screen.exitonclick()
