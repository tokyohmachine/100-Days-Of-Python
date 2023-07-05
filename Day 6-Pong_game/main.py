from turtle import Screen
from score_1 import Score
from paddles import Paddle
from ball import Ball
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)


r_paddles = Paddle((350, 0))
l_paddles = Paddle((-350, 0))
ball = Ball()
score = Score()

# keyboard
screen.listen()
screen.onkey(l_paddles.p_right, "a")
screen.onkey(l_paddles.pdr_down, "d")

screen.onkey(r_paddles.go_up, "Up")
screen.onkey(r_paddles.p_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # todo: Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # todo:Detect collision with paddle
    if ball.distance(r_paddles) < 50 and ball.xcor() > 320 or ball.distance(l_paddles) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    # todo: Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_increase_score()

    # todo: Detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_increase_score()


screen.exitonclick()