from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10
STARTING_MOVE_DISTANCE = 5

class carManager:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    # todo: Cars are randomly generated along the y-axis
    def car_generated(self):
        random_create = random.randint(1, 6)
        if random_create == 1:
            n_car = Turtle("square")
            n_car.shapesize(stretch_wid=1, stretch_len=2)
            n_car.penup()
            n_car.color(random.choice(COLORS))
            y = random.randint(-250, 250)
            n_car.goto(x=300, y=y)
            self.cars.append(n_car)

    def car_move(self):
        for car in self.cars:
            car.backward(self.car_speed)

    # todo: on the next level increase car
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT









