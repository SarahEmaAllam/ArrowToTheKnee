from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QStackedWidget
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide2.QtGui import QFont


class FinalWindow(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.setMinimumSize(QSize(800, 600))
        self.receiver = main_window

        self.layout = QVBoxLayout()

        font = QFont("Arial", 40, QFont.Bold)
        diagnosis = QLabel('Diagnosis:\n' + self.receiver.diagnosis)
        diagnosis.setFont(font)
        diagnosis.setAlignment(Qt.AlignHCenter)
        self.layout.addWidget(diagnosis)

        font = QFont("Arial", 20)
        treatment = QLabel(self.receiver.kb.treatments[self.receiver.diagnosis])
        treatment.setFont(font)
        treatment.setAlignment(Qt.AlignHCenter)
        self.layout.addWidget(treatment)

        button = QPushButton('Exit')
        button.clicked.connect(self.the_button_was_clicked)
        self.layout.addWidget(button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    # This function is the same in all other windows, because i just wanted to go through them iteratrively,
    # But here we have the answer which needs to go to the backend, and preferably return a question
    # back to here so we can send it back up to the Window Handler, which finds the corresponding index and
    # displays the question

    def the_button_was_clicked(self):
        exit(0)
