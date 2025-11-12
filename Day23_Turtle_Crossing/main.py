import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.onkey(player.move_forward, "Up")
screen.onkey(player.move_backward, "Down")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.drive()


    if player.ycor() > 280:
        scoreboard.level += 1
        scoreboard.update_level()
        player.goto(0, -280)
        car_manager.level_up()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
        if car.xcor() < -320:
            car_manager.all_cars.remove(car)

screen.exitonclick()