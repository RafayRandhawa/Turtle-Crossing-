import time
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

y_positions = []
for x in range(1,26):
    pos = 270 - (20*x)
    y_positions.append(pos)


class CarManager:

    def __init__(self):
        self.cars = []
        self.new_car = None
        self.level_num = 0

    def car_creation(self):
        chance = random.randint(1, 6)
        if chance == 6:
            self.new_car = Turtle()
            self.new_car.color(COLORS[random.randint(0, 5)])
            self.new_car.shape('square')
            self.new_car.penup()
            self.new_car.shapesize(1, 2)
            y = random.choice(y_positions)
            self.new_car.goto(305, y)
            self.cars.append(self.new_car)

    def move(self):
        for _ in self.cars:
            _.forward(-STARTING_MOVE_DISTANCE-(self.level_num*MOVE_INCREMENT))



