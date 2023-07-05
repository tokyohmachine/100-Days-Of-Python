
from turtle import Turtle
import random


bel = Turtle()
bel.width(15)   # size of each line
bel.speed(30)
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
radius = [0, 90, 180, 270] # degrees


while True:
    bel.color(random.choice(colors))
    bel.forward(40)             # paces
    bel.seth(random.choice(radius))



















