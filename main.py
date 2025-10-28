from turtle import Screen
from player import Player
from car_manager import Car
from scoreboard import Scoreboard
import time



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = Car()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            is_game_on = False
            scoreboard.game_over()

        if player.is_finishline():
            player.go_to_start()
            car_manager.level_up()
            scoreboard.increase_level()

screen.exitonclick()