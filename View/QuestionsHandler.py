from View.Button import Button
from View.Question import Question


# this class should handle all the existing questions :
# it retrieves the next question base don the KB priority
# it stashes already explored questions

class QuestionsHandler:
    def __init__(self):
        self.questions = []
        self.add_question(self.Question1("Does it croak?", "yes", "croak", "no", "sings"))

    def add_question(self, question):
        self.questions.append(question)

    def Question1(self, text, button1, symp1, button2, symp2):
        question = Question(text)
        self.add_question(question)
        question.create_button(button1, symp1)
        question.create_button(button2, symp2)
