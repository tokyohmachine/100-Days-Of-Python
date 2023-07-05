from turtle import Screen
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S.A States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guess_states = []
while len(guess_states) < 50:
    user_answers = turtle.textinput(f"{len(guess_states)}/50 States Correct", prompt="What's the State's name?").title()

    if user_answers == "Exit":
        missing_states = [state for state in all_states if state not in guess_states]
        print(missing_states)

        new_list_learn = pandas.DataFrame(missing_states)
        new_list_learn.to_csv("states_to_learn.cvs")

        break
    if user_answers in all_states:
        s = turtle.Turtle()
        s.hideturtle()
        s.penup()
        states_coord = data[data.state == user_answers]
        s.goto(int(states_coord.x), int(states_coord.y))
        s.write(user_answers)

turtle.mainloop()  # keep the screen open









