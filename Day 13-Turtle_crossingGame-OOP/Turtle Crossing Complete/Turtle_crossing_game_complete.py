from turtle import Screen, Turtle
import random
import time


# todo: setup screen
screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10
STARTING_MOVE_DISTANCE = 5


class carManager:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    #  todo: create random cars
    def car_generated(self):
        random_create = random.randint(1, 6)
        if random_create == 1:
            n_car = Turtle("square")
            n_car.color(random.choice(COLORS))
            n_car.shapesize(stretch_wid=1, stretch_len=2)
            n_car.penup()
            y = random.randint(-250, 250)
            n_car.goto(x=300, y=y)
            self.cars.append(n_car)

    # todo: move car
    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    # todo: on the next level increase car
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
COLORS_2 = ["red", "purple", "pink", "blue", "green"]


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color(random.choice(COLORS_2))
        self.penup()
        self.original_position()
        self.setheading(90)

    # todo: turtle moves forward
    def moving_up(self):
        self.forward(MOVE_DISTANCE)

    # todo: turtle moves back to the original position
    def original_position(self):
        self.goto(STARTING_POSITION)

    # todo: finish line
    def at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False


FONT = ("Courier", 18, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color("black")
        self.goto(x=-270, y=250)
        self.penup()
        self.update_scoreboard()

    # todo: update scoreboard
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    # todo: increase level
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    # todo: game over
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)


player = Player()
score = Score()
carManager = carManager()


# keywords display
screen.listen()
screen.onkey(player.moving_up, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # todo: create and move cars
    carManager.car_generated()
    carManager.move_cars()

    # todo: player collides with the cars
    for car in carManager.cars:
        if car.distance(player) < 15:
            game_is_on = False
            score.game_over()

    # todo: successful crossing
    if player.at_finish_line():
        player.original_position()
        carManager.increase_speed()
        score.increase_level()

screen.exitonclick()