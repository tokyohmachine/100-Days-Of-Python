from turtle import Turtle


FONT = ("courier", 18, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_player = 0
        self.right_player = 0


    def l_increase_score(self):
        self.left_player += 1
        self.update_score()
        self.clear()

    def r_increase_score(self):
        self.right_player += 1
        self.update_score()
        self.clear()

    def update_score(self):
        self.clear()
        self.goto(x=100, y=200)
        self.write(self.right_player, align="center", font=FONT)
        self.goto(x=-100, y=200)
        self.write(self.left_player, align="center", font=FONT)

    def game_over(self):
        self.goto(x=0, y=270)
        self.write("GAME OVER", align="center", font=FONT)




