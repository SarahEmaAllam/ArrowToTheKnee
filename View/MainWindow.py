from Button import Button
from PySide2.QtCore import QSize
from PySide2.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget
from View.Question import Question

# Subclass MainWindow to customize the application's main window
from QuestionsHandler import QuestionsHandler
from Model.ForwardChaining import *


class MainWindow(QMainWindow):
    # Passed parameters: window title, QuestionHandler containing all question objects
    def __init__(self, title, questions):
        super().__init__()

        self.setWindowTitle(title)
        self.setMinimumSize(QSize(400, 300))
        self.questions = questions
        self.patient = None

    # Method to call forward chaining, which at the end calls update_window
    # TODO: patient parameter for f_c, not sure how the patient class is used in current algorithm
    # TODO: adapt such that it doesn't call f_c for questions where you can select multiple
    def was_clicked(self):
        forward_chaining(self, self.patient)

    # Method to update the window with the next question retrieved from the priority queue
    def update_window(self, question, patient):
        self.patient = patient
        layout = QVBoxLayout()
        layout.addWidget(QLabel(question.question))
        for button in question.buttons:
            layout.addWidget(button)
            # Connect every added button to method was_clicked so that fc is called for each of them
            button.clicked.connect(self.was_clicked)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.update()
