import sys
from PySide2.QtWidgets import QApplication
from View.MainWindow import MainWindow
from Model.ForwardChaining import *


app = QApplication(sys.argv)

# Create QuestionHandler that reads all questions from a .txt file
questions = QuestionsHandler()
questions.initialize_questions()

window = MainWindow("Knee Issues", questions)
window.show()

# First question is popped and sent to view which in turn calls FC when a button is clicked
question = questions.pop()
window.update_window(question)
app.exec_()
