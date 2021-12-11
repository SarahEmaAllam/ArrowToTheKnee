from Button import Button
from PySide2.QtCore import QSize
from PySide2.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget
from View.Question import Question

# Subclass MainWindow to customize the application's main window
from QuestionsHandler import QuestionsHandler
from Model.ForwardChaining import *


class MainWindow(QMainWindow):
    def __init__(self, title, questions):
        super().__init__()

        self.setWindowTitle(title)

        self.setMinimumSize(QSize(400, 300))

        self.questions = questions

        self.symptom = []

        self.current_question = None

    # Method to define window behavior when button is clicked (could be used to change buttons/question)
    # MISSING: patient parameter for f_c, not sure how the patient class is used in current algorithm
    def was_clicked(self):
        print(self.sender().symptom)
        forward_chaining(self, None)

    def update_window(self, question):
        self.current_question = question
        layout = QVBoxLayout()
        layout.addWidget(QLabel(self.current_question.question))
        for button in self.current_question.buttons:
            layout.addWidget(button)
            button.clicked.connect(self.was_clicked)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.update()
