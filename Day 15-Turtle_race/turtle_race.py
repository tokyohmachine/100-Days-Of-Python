import turtle
from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make our bet", prompt="which turtle will win the race? Enter a color: ")
color = ["red", "orange", "purple", "green", "pink", "blue"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_number in range(0, 6):
    new_turtles = Turtle(shape="turtle")
    new_turtles.color(color[turtle_number])
    new_turtles.penup()
    new_turtles.goto(x=-230, y=y_position[turtle_number])
    all_turtles.append(new_turtles)

if bet:
    race_on = True

while race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            win_color = turtle.pencolor()
            if win_color == bet:
                print(f"You've won! The {win_color} turtle is the winner!")
            else:
                print(f"You've lost. The {win_color} turtle is the winner!")

        distance = random.randint(0, 10)
        turtle.forward(distance)


screen.exitonclick()