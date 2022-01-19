from PySide2.QtWidgets import QSlider
from PySide2.QtCore import Qt


# Subclass of QSlider to customize the application's sliders
class Slider(QSlider):

    def __init__(self, symptom):
        super().__init__()
        self.setOrientation(Qt.Horizontal)
        self.setTickInterval(1)
        self.setTickPosition(QSlider.TicksAbove)
        self.setRange(0, 5)
        self.setMinimum(0)
        self.setMaximum(5)
        self.symptom = symptom

