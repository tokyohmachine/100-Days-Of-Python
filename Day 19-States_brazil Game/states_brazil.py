from turtle import Screen
import turtle
import pandas


# todo 1: setup screen and add image
screen = turtle.Screen()
screen.title("Guessing Brazil States Game")
image = "brasil_image.gif"
screen.addshape(image)
turtle.shape(image)


# todo 2: call pandas read cvs e create a list with all states
data = pandas.read_csv("26_state.csv")
all_states = data.state.to_list()


# create an empty list
# pop up a screen to the user guess the states
# check if the guess is among 26 states/ keep track of the score
# convert the guess to Title case
# write correct guesses onto the map
# use a loop to allow the user to keep guessing
# record the correct guesses in a list
# todo 3: create an attribute to the turtle e methods in turtle/ do not forget the coordenates
# compare the states list with the user's guess
# todo 4: turtle input for user answer the state's names e count the number of states already guessed
# todo 5: create a way to get out of the loop
# todo 6: create a new file with pandas.Dataframe with the states you missed
guessed_states = []
while len(guessed_states) < 26:
    user_answer=turtle.textinput(f"{len(guessed_states)}/26 States Correct", prompt="What's the state's name?").title()

    if user_answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        print(missing_states)

        new_file = pandas.DataFrame(missing_states)
        new_file.to_csv("Missing_states.cvs")

        break
    if user_answer in all_states:
        guessed_states.append(user_answer)
        b = turtle.Turtle()
        b.penup()
        states_b = data[data.state == user_answer]
        b.goto(int(states_b.x), int(states_b.y))
        b.write(user_answer)


turtle.mainloop()

