from .Button import Button
from PySide2.QtCore import QSize
from PySide2.QtWidgets import QMainWindow
from View.Question import Question

# Subclass MainWindow to customize the application's main window
from QuestionsHandler import QuestionsHandler


class MainWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()

        self.setWindowTitle(title)

        # button = Button("yo", False)

        # button.clicked.connect(self.was_clicked)

        self.setMinimumSize(QSize(400, 300))

        questions = QuestionsHandler()
        questions.add_to_window(self)

    # Method to define window behavior when button is clicked (could be used to change buttons/question)
    def was_clicked(self):
        self.setWindowTitle("Button Clicked")

