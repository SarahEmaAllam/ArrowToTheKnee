from View.Button import *
from Model.ForwardChaining import *
from View.Slider import *


class Window(QMainWindow):
    def __init__(self, main_window, question, widgets, qtype="normal"):
        super().__init__()
        self.main_window = main_window
        self.setMinimumSize(QSize(600, 400))
        self.layout = QVBoxLayout()
        self.question = question
        self.qtype = qtype
        self.widgets = []
        self.symptoms = []

        self.set_widgets(widgets)
        self.construct_window()

    def set_widgets(self, widgets):
        if self.qtype == "normal":
            for button in widgets:
                new_button = Button(button[0], button[1])
                # Connect every added button to method was_clicked so that fc is called for each of them
                new_button.clicked.connect(self.was_clicked)
                self.widgets.append(new_button)

        elif self.qtype == "multi":
            for button in widgets:
                new_slider = Slider()
                new_button = Button(button[0], button[1])
                new_slider.valueChanged.connect(new_button.change_value)
                new_button.setCheckable(True)
                new_button.clicked.connect(self.was_clicked_checkable)
                self.widgets.append(new_button)
                self.widgets.append(new_slider)
            new_button = Button("Next", "next")
            new_button.clicked.connect(self.was_clicked)
            self.widgets.append(new_button)

        if self.main_window.diagnosis:
            diagnosis = QLabel()
            diagnosis.setText("Temporary Diagnosis: " + self.main_window.diagnosis)
            self.widgets.append(diagnosis)

    def was_clicked(self):
        if self.sender().text() != "Next":
            self.symptoms.append(self.sender().symptom)

        stack = self.main_window.stack
        if self.sender().text() == "No":
            if self.question == "Does bending or extending the knee hurt?" or self.question == "Is there swelling of " \
                                                                                               "the knee?":
                stack.removeWidget(stack.widget(stack.currentIndex() + 1))

        print("current ques", self.question)
        print("HEYEYEYEYEY ", self.symptoms)
        # forward_chaining(self, self.main_window.patient)
        self.main_window.show_next_screen()

    def was_clicked_checkable(self, checked):
        if checked:
            self.symptoms.append([self.sender().symptom, self.sender().slider_value])
        else:
            for symptom in self.symptoms:
                if symptom[0] == self.sender().symptom:
                    self.symptoms.remove(symptom)

    def construct_window(self):
        self.layout.addWidget(QLabel(self.question))
        for widget in self.widgets:
            self.layout.addWidget(widget)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
