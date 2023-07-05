import turtle
from turtle import Turtle, Screen
import random

s = Turtle()
s.speed(30)


def color():
    turtle.colormode(255)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    s.color(r, g, b)


for each_circle in range(100):
    s.circle(100)
    color()
    s.left(360 / 100)

screen = Screen()
screen.exitonclick()