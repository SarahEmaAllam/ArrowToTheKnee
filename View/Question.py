
class Question(object):
    def __init__(self):
        self.question = ""
        self.buttons = []

    def set_question(self, question):
        self.question = question

    def add_button(self, button):
        self.buttons.append(button)
