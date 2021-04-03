from turtle import Turtle, Screen
import random
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

trix = Turtle()

trix.shape("turtle")
for i in range(3, 10):
    angle = 360/i
    trix.color(random.choice(colours))
    for j in range(i):
        trix.forward(100)
        trix.right(angle)

screen = Screen()
screen.exitonclick()