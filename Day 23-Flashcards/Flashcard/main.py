from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# Todo 2: Random the words
# Read the data from the french_words.csv file in the data folder
# Pick a random French word/translation and put the word into the flashcard. Every time you press the ❌ or ✅ buttons,
# it should generate a new random word to display. e.g.
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(background, image=front_image)
    flip_timer = window.after(ms=3000, func=flip_card)


# Todo 3: Flip the cards
# After a delay of 3s (3000ms), the card should flip and display the English translation for the current word
# The card image should change to the card_back.png and the text colour should change to white.
# The title of the card should change to "English" from "French"
def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(background, image=back_image)

# Todo 4: Save Your Progress
# When the user presses on the ✅ button, it means that they know the current word on the
# flashcard and that word should be removed from the list of words that might come up
# create a file from scratch with pandas.Dataframe()  to_cvs()

# check if there is a words_to_learn.csv file. If it exists,
# the program should use those words to put on the flashcards. If the
# words_to_learn.csv does not exist (i.e., the first time the program is run),
# then it should use the words in the french_words.csv

def remove_cards_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()


# ________________________________________________________ SETUP UI___________________________________________________________ #
# Todo 1:

window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(ms=3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="card_front.png")
back_image = PhotoImage(file="card_back.png")
background = canvas.create_image(400, 263, image=front_image)

title_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# buttons
wrong_image = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="right.png")
right_button = Button(image=right_image, highlightthickness=0, command=remove_cards_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
