from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.speed(0)
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)


    def go_up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def p_down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(y), y)


    def p_right(self):
        y = self.ycor() + 20
        self.goto(self.ycor(), y)

    def pdr_down(self):
        y = self.ycor() - 20
        self.goto(self.ycor(), y)



















