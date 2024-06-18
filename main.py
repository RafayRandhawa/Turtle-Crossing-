import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.move, 'Up')
game_is_on = True
no_collision = True

while no_collision:
    level = scoreboard.current_level()
    for x in range(0, level):
        car_manager.car_creation()
    car_manager.move()
    for _ in car_manager.cars:
        if player.distance(_) < 20:
            no_collision = False
    if player.finish_line():
        scoreboard.level_up()
        car_manager.level_num += 1
    else:
        pass
    scoreboard.score_write()
    time.sleep(0.1)
    screen.update()
scoreboard.game_over()
screen.exitonclick()
