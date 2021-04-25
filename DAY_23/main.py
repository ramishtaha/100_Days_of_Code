import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.move_player, "Up")
cars = []
scoreboard = Scoreboard()
flag = 1
game_speed = 0.1

game_is_on = True
while game_is_on:
    time.sleep(game_speed)
    flag += 1
    if flag % 6 == 0:
        cars.append(CarManager())

    # while car.xcor() > 300:
    #     car.move_car()
    for car in cars:
        car.move_car()
        if player.distance(car) < 21:
            game_is_on = False

    if player.ycor() > 290:
        player.respawn()
        game_speed /= 2
        scoreboard.level_up()




    screen.update()
scoreboard.game_over()

screen.exitonclick()