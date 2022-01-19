from PySide2.QtWidgets import QPushButton


# Subclass of QPushButton to customize the application's buttons
class Button(QPushButton):

    def __init__(self, text, symptom):
        super().__init__(text)
        self.symptom = symptom
