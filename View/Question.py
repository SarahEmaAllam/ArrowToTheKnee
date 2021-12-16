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
    def __init__(self, question="", variable = '',  parent=None):
        super().__init__()
        self.parent = parent  # the previous question, keep track of the branching
        # ^ currently already sorta done by explored in QuestionHandler i think
        self.question = question
        self.variable = variable
        self.buttons = []

    def set_question(self, question):
        self.question = question

    def add_button(self, button):
        self.buttons.append(button)

    # button should represent a symptom in the KB
    def create_button(self, text, symptom):
        # vbox = QVBoxLayout()
        button = Button(text, symptom)  # the text that will appear on the button
        self.add_button(button)
