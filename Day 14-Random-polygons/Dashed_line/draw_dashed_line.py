from turtle import Turtle, Screen


bel = Turtle()
bel.color("black")

for _ in range(15):      # repeat 15x
    bel.forward(10)      # 10 paces
    bel.penup()          # no drawing when moving
    bel.forward(10)
    bel.pendown()        # drawing when moving.


screen = Screen()
screen.exitonclick()