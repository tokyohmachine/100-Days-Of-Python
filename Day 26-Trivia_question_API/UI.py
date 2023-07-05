from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
check_answer: str

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.text = self.canvas.create_text(150, 125, width=280, text="word", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        image_true = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=image_true, highlightthickness=0, command=self.true_click)
        self.true_button.grid(row=2, column=0)

        image_false = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=image_false, highlightthickness=0, command=self.false_click)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="You have reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_click(self):
        self.feedback(self.quiz.check_answer("True"))

    def false_click(self):
        correct = self.quiz.check_answer("False")
        self.feedback(correct)

    def feedback(self, correct):
        if correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



