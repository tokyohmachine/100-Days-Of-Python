from turtle import Turtle
import random

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
COLORS = ["red", "purple", "pink", "blue", "green"]

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color(random.choice(COLORS))
        self.penup()
        self.move_start_point()
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE) # 10

    # todo: turtle moves back to the original position
    def move_start_point(self):
        self.goto(STARTING_POSITION)

    def at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False



