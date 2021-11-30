from .Button import Button
from PySide2.QtCore import QSize
from PySide2.QtWidgets import QMainWindow


# Subclass MainWindow to customize the application's main window
class MainWindow(QMainWindow):
    def __init__(self, title):
        super().__init__()

        self.setWindowTitle(title)

        button = Button("yo", False)

        button.clicked.connect(self.was_clicked)

        self.setMinimumSize(QSize(400, 300))

        button.add_to_window(self)

    # Method to define window behavior when button is clicked (could be used to change buttons/question)
    def was_clicked(self):
        self.setWindowTitle("Button Clicked")
