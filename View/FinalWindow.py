from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QLabel, QVBoxLayout, QWidget, QStackedWidget
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide2.QtGui import QFont


# Subclass of QMainWindow to customize the application's final window
class FinalWindow(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        # Standard window settings
        self.setMinimumSize(QSize(1000, 600))
        self.layout = QVBoxLayout()

        self.receiver = main_window

        font = QFont("Arial", 30, QFont.Bold)
        diagnosis = QLabel('Diagnosis:\n' + self.receiver.diagnosis)
        diagnosis.setFont(font)
        diagnosis.setAlignment(Qt.AlignHCenter)
        self.layout.addWidget(diagnosis)

        font = QFont("Arial", 15)
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

    # Function defining button behavior when clicked
    def the_button_was_clicked(self):
        exit(0)
