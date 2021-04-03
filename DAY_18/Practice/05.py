import turtle as t
import random

trix = t.Turtle()
t.colormode(255)
def rand_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

trix.shape("turtle")
trix.width(5)
trix.speed("fastest")
for _ in range(20):
    trix.color(rand_color())
    trix.circle(100)
    trix.right(18)

screen = t.Screen()
screen.exitonclick()