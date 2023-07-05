from turtle import Turtle, Screen


bel = Turtle()
bel.color("white")
screen = Screen()
screen.bgcolor("black")


def move_forward():
    bel.forward(10)

def move_back():
    bel.backward(10)


def counter_clock():
    left = bel.heading() + 10
    bel.seth(left)


def clockwise():
    right = bel.heading() - 10
    bel.seth(right)


def clear():
    bel.clear()
    bel.penup()
    bel.home()
    bel.pendown()


screen.listen()
screen.onkey(move_forward, "f")
screen.onkey(move_back, "b")
screen.onkey(counter_clock, "l")
screen.onkey(clockwise, "r")
screen.onkey(clear, "c")
clear()

screen.exitonclick()