from turtle import Screen, Turtle
import turtle
import pandas


# todo 1: setup screen and add image
screen = Screen()
screen.title("Guessing Brazil States Game")
image = "Brasil_Map.gif"
screen.addshape(image)
turtle.shape(image)


def get_mouse_click_coord(x, y):
    print(x, y)
turtle.onscreenclick(get_mouse_click_coord)


screen.mainloop()