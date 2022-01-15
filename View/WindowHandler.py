from PySide2.QtWidgets import QStackedWidget
from View.Window import *
from View.IntroductionWindow import *
from View.FinalWindow import *


class WindowHandler:
    def __init__(self, knowledge_base):
        self.stack = QStackedWidget()
        self.kb = knowledge_base
        self.diagnosis = ""
        self.start = True
        self.idx = 0
        self.set_window()
        self.stack.show()

    def set_window(self):
        questions = self.kb.questions
        if self.start:
            self.stack.addWidget(IntroductionWindow(self))
            self.start = False
        elif self.idx >= len(questions):
            self.stack.addWidget(FinalWindow(self))
        else:
            # print(question[1], question[2], question[3])
            print("question[0] should be the key variable", questions[self.idx][0])
            new_window = Window(self, questions[self.idx][0], questions[self.idx][1], questions[self.idx][2])
            self.stack.addWidget(new_window)
            self.idx += 1

    def show_next_screen(self):
        self.set_window()
        print(self.stack.currentIndex())
        self.stack.setCurrentIndex(self.stack.currentIndex() + 1)
        self.stack.widget(self.stack.currentIndex()).diagnosis = self.diagnosis
        self.stack.show()
