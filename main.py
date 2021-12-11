import sys
from PySide2.QtWidgets import QApplication
from View.MainWindow import MainWindow
from Model.ForwardChaining import *
from Model.Patient import Patient


app = QApplication(sys.argv)

questions = QuestionsHandler()
questions.initialize_questions()

window = MainWindow("Knee Issues", questions)
window.show()

patient = Patient()

question = questions.pop()
window.update_window(question)
app.exec_()
