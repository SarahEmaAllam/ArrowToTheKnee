from View.Button import *
from Model.ForwardChaining import *
from View.Slider import *
from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QWidget, QSizePolicy
from PySide2.QtCore import QSize
from PySide2.QtGui import QFont


# Subclass of QMainWindow to customize the application's question windows
class Window(QMainWindow):
    def __init__(self, main_window, question, widgets, qtype):
        super().__init__()
        # Standard window settings
        self.main_window = main_window
        self.setMinimumSize(QSize(1000, 600))
        self.layout = QVBoxLayout()

        self.question = question
        self.qtype = qtype
        self.widgets = []
        self.symptoms = []

        # Construct window
        self.set_widgets(widgets)
        self.construct_window()

    # Function for constructing the elements of a window
    def set_widgets(self, widgets):
        # Standard window buttons
        if self.qtype == "normal":
            for button in widgets:
                new_button = Button(button[0], button[1])
                new_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
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

        # Show temporary diagnosis if there is one
        if self.main_window.diagnosis:
            diagnosis = QLabel()
            diagnosis.setText("Temporary Diagnosis: " + self.main_window.diagnosis)
            self.widgets.append(diagnosis)

    # Function defining button behavior when clicked, calls forward chaining process
    def was_clicked(self):

        if self.sender().text() == "Next":
            if not self.symptoms:
                # Statement to ensure no error is met when sliders are not adjusted
                self.symptoms.append(["still", 0])
        else:
            self.symptoms.append(self.sender().symptom)

        # Skip follow-up question whenever it is irrelevant
        if self.sender().text() == "No":
            if self.question == "Does bending or extending the knee hurt?" or self.question == "Is there swelling of " \
                                                                                               "the knee?":
                self.main_window.idx += 1

        # Store result of forward chaining with obtained facts as temporary diagnosis
        temp_diagnosis = forward_chaining(self, self.main_window.kb, self.symptoms)
        self.main_window.diagnosis = temp_diagnosis
        self.main_window.show_next_screen()

    # Function defining slider behavior
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

    # Function that constructs the window
    def construct_window(self):
        text_label = QLabel(self.question)
        text_label.setAlignment(Qt.AlignCenter)
        text_label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        font = QFont("Cambria", 25, QFont.Bold)
        text_label.setFont(font)
        self.layout.addWidget(text_label)

        for widget in self.widgets:
            self.layout.addWidget(widget)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
