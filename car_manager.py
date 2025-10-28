from turtle import Turtle, colormode
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

def car_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

colormode(255)

class Car:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(car_colors())
            new_car.penup()
            new_car.shapesize(1,2)
            new_car.speed(0)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(MOVE_INCREMENT)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

