import time
from turtle import Screen
from player import Player
from car_manager import carManager
from score_ import Score

screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)


car_manager = carManager()
player = Player()
score = Score()


# turtle moves forward
screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # todo: create and move cars
    car_manager.car_generated()
    car_manager.car_move()

    # todo: player collides with the cars
    for car in car_manager.cars:
        if car.distance(player) < 15:
            game_is_on = False
            score.game_over()

    # todo: successful crossing
    if player.at_finish_line():
        player.move_start_point()
        car_manager.increase_speed()
        score.increase_level()


screen.exitonclick()