from PySide2.QtWidgets import QPushButton


# Subclass of QPushButton to customize the application's QPushButtons
class Button(QPushButton):

    def __init__(self, text, symptom):
        super().__init__(text)
        self.setCheckable(True)
        self.symptom = symptom
        # if clicked, add symptom to KB
        self.clicked.connect(self.was_clicked)

    # Method defining behavior when a button is clicked
    def was_clicked(self):
        # self.setText("I was clicked")
        self.setEnabled(False)


    # Method that adds the button to the window (needs adjustment to fit layout)
    def add_to_window(self, window):
        window.setCentralWidget(self)
