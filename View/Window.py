from View.Button import *
from Model.ForwardChaining2 import *
from View.Slider import *

# current_diagnosis = 'None'


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
        # Standard window buttons
        if self.qtype == "normal":
            for button in widgets:
                new_button = Button(button[0], button[1])
                # Connect every added button to method was_clicked so that fc is called for each of them
                new_button.clicked.connect(self.was_clicked)
                self.widgets.append(new_button)

        # Multi choice: text labels with sliders
        elif self.qtype == "multi":
            for slider in widgets:
                # Create text label for movement type
                new_label = QLabel(slider[0])
                new_label.setAlignment(Qt.AlignHCenter)
                self.widgets.append(new_label)

                # Create slider with symptom key
                new_slider = Slider(slider[1])
                new_slider.valueChanged.connect(self.value_changed)
                self.widgets.append(new_slider)

            # Create "next" button that calls was_clicked (fc)
            new_button = Button("Next", "next")
            new_button.clicked.connect(self.was_clicked)
            self.widgets.append(new_button)

        # diagnosis = QLabel()
        # diagnosis.setText("Temporary Diagnosis: " + current_diagnosis)
        # self.widgets.append(diagnosis)

        # Show temporary diagnosis if there is one
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
        result = forward_chaining(self, self.main_window.kb, self.symptoms)
        print('current diaf', result)
        self.main_window.diagnosis = result
        self.main_window.show_next_screen()

    def value_changed(self):
        # Iterates through the already found values for sliders
        for symptom in self.symptoms:
            if symptom[0] == self.sender().symptom:
                # Remove from symptom list if slider value = 0
                if self.sender().value() == 0:
                    self.symptoms.remove(symptom)
                # Change symptom value if slider value nonzero
                else:
                    symptom[1] = str(self.sender().value())
                return
        # Add new nonzero symptom value to list
        self.symptoms.append([self.sender().symptom, str(self.sender().value())])

    def construct_window(self):
        self.layout.addWidget(QLabel(self.question))
        for widget in self.widgets:
            self.layout.addWidget(widget)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
