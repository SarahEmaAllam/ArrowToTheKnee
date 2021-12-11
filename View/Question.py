import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import (
    QMessageBox,
)
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QGroupBox, QGridLayout
import sys
from PySide2.QtGui import QIcon, QFont

from View.Button import Button


class Question(QWidget):
    def __init__(self, weight=1, question="", parent=None):
        super().__init__()
        self.weight = weight  # should be initialized with a base one and updated
        self.parent = parent  # the previous question, keep track of the branching
        # ^ currently already sorta done by explored in QuestionHandler i think
        self.question = question
        self.buttons = []

    def __lt__(self, other):  # defines weight priority
        return self.weight < other.weight

    def set_weight(self, weight):
        self.weight = weight

    def set_question(self, question):
        self.question = question

    def add_button(self, button):
        self.buttons.append(button)

    # button should represent a symptom in the KB
    def create_button(self, text, symptom):
        # vbox = QVBoxLayout()
        button = Button(text, symptom)  # the text that will appear on the button
        self.add_button(button)
