from View.Window import *
from View.IntroductionWindow import *
from View.FinalWindow import *


# Class that handles the initialization and changing of windows
class WindowHandler:
    def __init__(self, knowledge_base):
        self.stack = QStackedWidget()
        self.kb = knowledge_base
        self.diagnosis = ""
        self.start = True
        self.idx = 0

        self.set_window()
        self.stack.show()

    # Function intializing a single window
    def set_window(self):
        questions = self.kb.questions

        if self.start:
            self.stack.addWidget(IntroductionWindow(self))
            self.start = False

        elif self.idx >= len(questions):
            self.stack.addWidget(FinalWindow(self))

        else:
            new_window = Window(self, questions[self.idx][0], questions[self.idx][1], questions[self.idx][2])
            self.stack.addWidget(new_window)
            self.idx += 1

    # Function changing the window to the next one in the stack
    def show_next_screen(self):
        self.set_window()
        self.stack.setCurrentIndex(self.stack.currentIndex() + 1)
        self.stack.widget(self.stack.currentIndex()).diagnosis = self.diagnosis
        self.stack.show()
