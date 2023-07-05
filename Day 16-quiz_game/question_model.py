class Question:

    def __init__(self, question, correct_answer):
        self.text = question
        self.answer = correct_answer


new_question = Question("sdf sdf", "False")
print(new_question)