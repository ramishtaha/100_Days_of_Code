import turtle as t
import random

trix = t.Turtle()
t.colormode(255)
def rand_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

trix.shape("turtle")
trix.width(10)
trix.speed(random.randint(8, 10))
for _ in range(200):
    trix.color(rand_color())
    angle = 90 * random.randint(1, 4)
    trix.forward(30)
    trix.setheading(angle)

screen = t.Screen()
screen.exitonclick()