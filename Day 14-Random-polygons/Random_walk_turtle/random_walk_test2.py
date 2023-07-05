import random
import turtle

billie = turtle.Turtle()
billie.hideturtle()
billie.pensize(15)
billie.speed(30)


def random_color():
    turtle.colormode(255)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    billie.color(r, g, b)


radius = [0, 90, 180, 270]


while True:
    random_color()
    billie.forward(40)
    billie.setheading(random.choice(radius))