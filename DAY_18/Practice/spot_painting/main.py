import turtle as t
import random
import

trix = t.Turtle()
t.colormode(255)
def rand_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

trix.shape("turtle")
trix.width(5)
trix.speed("fastest")