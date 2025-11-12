from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 6
LANES = range(-200, 260, 20)

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def drive(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2)
            random_y = random.choice(LANES)
            new_car.goto(340, random_y)
            self.all_cars.append(new_car)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT