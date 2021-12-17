import sys
from PySide2.QtWidgets import QApplication
from View.MainWindow import MainWindow
from Model.ForwardChaining import *
from Model.Patient import Patient

var = False

dict = [(var, 1)]
print(dict)

var = True
print(dict)

app = QApplication(sys.argv)

kb = KnowledgeBase()
# Create QuestionHandler that reads all questions from a .txt file
questions = QuestionsHandler(kb)
question = questions.questions.pop()

window = MainWindow("Knee Issues", questions, question, kb)
window.show()

# First question is popped and sent to view which in turn calls FC when a button is clicked
patient = Patient()
window.update_window(question, patient)

# Start the event queue (show the first question in the window)
app.exec_()
