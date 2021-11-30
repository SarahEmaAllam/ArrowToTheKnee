import sys
from PySide2.QtWidgets import QApplication
from View.MainWindow import MainWindow
from Model.ForwardChaining import *
from Model.Patient import Patient


# app = QApplication(sys.argv)

# window = MainWindow("title")
# window.show()

# app.exec_()

patient = Patient(["male", "old"])
forward_chaining(patient)
