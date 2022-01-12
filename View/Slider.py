from PySide2.QtWidgets import QSlider


# Subclass of QPushButton to customize the application's QPushButtons
class Slider(QSlider):

    def __init__(self, symptom):
        super().__init__()
        self.symptom = symptom
        self.setMinimum(1)
        self.setMaximum(5)
        self.val = '1'
        # if clicked, add symptom to KB
        self.valueChanged.connect(self.change_value())

    # Method defining behavior when a button is clicked
    def change_value(self):
        self.val = str(self.value())
