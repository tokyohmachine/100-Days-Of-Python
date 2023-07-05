import random
import turtle

PAINT_SPEED = 30
PAINT_SIZE = 20
DOT_DISTANCE = 50
NUM_DOTS = 100
COLORS = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185),
          (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158),
          (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20),
          (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

paint = turtle.Turtle()
turtle.colormode(255)
paint.penup()
paint.speed(PAINT_SPEED)
paint.hideturtle()

paint.setheading(225)
paint.forward(300)
paint.setheading(0)

for dot_number in range(1, NUM_DOTS + 1):
    paint.dot(PAINT_SIZE, random.choice(COLORS))
    paint.forward(DOT_DISTANCE)

    if dot_number % 10 == 0:
        paint.setheading(90)
        paint.forward(DOT_DISTANCE)
        paint.setheading(180)
        paint.forward(DOT_DISTANCE * 10)
        paint.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
