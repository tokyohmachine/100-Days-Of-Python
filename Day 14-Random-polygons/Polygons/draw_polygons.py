from turtle import Turtle, Screen
import random

bel = Turtle()
colors = ["spring green", "deep pink", "teal", "dodger blue", "gold", "dark violet", "red", "DeepSkyBlue", "wheat", "DarkOrchid"]


def draw_poly(sides):
    for _ in range(sides):
        angle = 360
        bel.forward(100)
        bel.right(angle / sides)  # 360/sides

# quantidade de lados


for each_side in range(3, 11):  # all the sides of polygons
    bel.color(random.choice(colors))     # random colors
    draw_poly(each_side)                 # call the function with each side inside


screen = Screen()
screen.exitonclick()
