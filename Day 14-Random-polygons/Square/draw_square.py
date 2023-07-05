from turtle import Turtle, Screen


bel = Turtle()
#bel.shape("turtle")
bel.color("red")

for each_side_square in range(4):
    bel.forward(100)
    bel.left(90)

screen = Screen()
screen.exitonclick()