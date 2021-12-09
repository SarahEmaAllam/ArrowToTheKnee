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
    def __init__(self, question, weight, parent):
        super().__init__()
        self.weight = weight  # should be initialized with a base one and updated
        self.parent = parent  # the previous question, keep track of the branching
        self.question = question
        self.buttons = []
        self.answers = []
        self.selected_answer = None

    def __lt__(self, other):  # defines weight priority
        return self.weight < other.weight

    def add_button(self, button):
        self.buttons.append(button)

    # button should represent a symptom in the KB
    def create_button(self, text, symptom):
        vbox = QVBoxLayout()
        btn = Button(text, symptom)  # the text that will appear on the button
        button = (btn, symptom)
        self.add_button(button)







