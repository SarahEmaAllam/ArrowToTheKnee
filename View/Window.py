from View.Button import *
from Model.ForwardChaining import *
from View.Slider import *


class Window(QMainWindow):
    def __init__(self, main_window, question, buttons, qtype="normal"):
        super().__init__()
        self.main_window = main_window
        self.setMinimumSize(QSize(400, 300))
        self.layout = QVBoxLayout()
        self.question = question
        self.qtype = qtype
        self.buttons = []
        self.symptoms = []

        self.set_buttons(buttons)
        self.construct_window()

    def set_buttons(self, buttons):
        for button in buttons:
            new_button = Button(button[0], button[1])
            self.buttons.append(new_button)

    def was_clicked(self):
        if self.qtype == "normal":
            print("current ques", self.question)
            print("HEYEYEYEYEY ", self.sender().symptom)
            # forward_chaining(self, self.main_window.patient)
            self.main_window.show_next_screen()

    def construct_window(self):
        self.layout.addWidget(QLabel(self.question))
        if self.qtype == "normal":
            for button in self.buttons:
                # Connect every added button to method was_clicked so that fc is called for each of them
                button.clicked.connect(self.was_clicked)
                self.layout.addWidget(button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
