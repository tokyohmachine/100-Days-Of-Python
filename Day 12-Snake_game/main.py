from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

# TODO 1: create two squares 600 x 600
screen = Screen()
screen.title("Snake Game")
screen.bgcolor("black")  # background of the game
screen.setup(width=600, height=600)  # pixels of the screen
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "u")
screen.onkey(snake.down, "d")
screen.onkey(snake.left, "l")
screen.onkey(snake.right, "r")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # todo: detecting collision food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend_tail()
        score.increase_score()

    # todo: detecting collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        score.game_over()

    # todo: detecting collision with tail
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()


screen.exitonclick()