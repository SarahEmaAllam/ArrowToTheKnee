import sys
from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton

#A Dictionary that holds all Questions:Answer pairs.

questions = {'age_question':['0-12','12-18','18-39','39-55','55+'],
             'gender_question':['Male','Female'],
             'pain_start_question':['Gradually','Suddenly'],
             'pain_location_question':['Front','Inner Side','Outer Side','Backside','Within'],
             'swelling_question':['Yes','No','Sometimes'],
             'bending_question':['Yes', 'No'],
             'activities_question': ['Explosive Movements','Repeated Movements', 'Movement with torsions', 'Sitting still', 'All of the above'],
             'swelling_location_question': ['In one spot', 'Whole Knee'],
             'extension_question': ['When extending the knee', 'When bending the knee', 'Both']         
              }


#I know this is a horrible way to do it
#A function to match a question string to question class, also might not need it depending on implementation
def matchQuestionToWindow(Question):
    if(Question== 'age_question'):
        Window = AgeWindow()
        return Window
    elif(Question == 'gender_question'):
        Window = GenderWindow()
        return Window
    elif(Question == 'pain_start_question'):
        Window = PainStartWindow()
        return Window
    elif(Question == 'pain_location_question'):
        Window = PainLocationWindow()
        return Window
    elif(Question == 'swelling_question'):
        Window = SwellingLocationWindow()
        return Window
    elif(Question == 'extension_question'):
        Window = ExtensionWindow()
        return Window
    elif(Question == 'bending_question'):
        Window = BendingWindow()
        return Window
    elif(Question == 'activities_question'):
        Window = GenderWindow()
        return Window
    else:
        print("Question not there")


#Just trying out something here
class WindowHandler:
    def __init__(self, window):
        self.window = window

    def changeWindow(self, new_window):
        self.window = new_window

    def makeWindow(self):
        self.window.show()

    def test(self):
        print('test')

#Different Windows, Might be good to have them as individual classes but that depends on overall implement
#Implementation

class IntroductionWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.IDx = 'introduction_question'
            self.start = False
            self.answers = 'intro'
            self.setMinimumSize(QSize(400, 300))

            self.layout = QVBoxLayout()

            self.layout.addWidget(QLabel('Did you recently take an arrow to the knee?'))

            button = QPushButton('Yes please help')
            button.setCheckable(True)
            button.clicked.connect(self.the_button_was_clicked)
            button = self.layout.addWidget(button)

            container = QWidget()
            container.setLayout(self.layout)
            self.setCentralWidget(container)

        def the_button_was_clicked(self):
            #send the answer to FC
            pass
            #receive new question#

# Subclass QMainWindow to customize your application's main window
class AgeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.IDx = 'age_question'
        self.setStyleSheet("background-color: #5B5A5A")
        self.answers = questions[self.IDx]
        self.setMinimumSize(QSize(400, 300))

        self.layout = QVBoxLayout()

        self.layout.addWidget(QLabel('What is your Age?'))

        for answer in range(len(self.answers)):
            button = QPushButton(questions[self.IDx][answer])
            button.setCheckable(True)
            button.clicked.connect(self.the_button_was_clicked)
            button = self.layout.addWidget(button)


        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)


        # Set the central widget of the Window.
        #self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print (self.IDx, self.sender().text())

class GenderWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.IDx = 'gender_question'
        self.answers = questions[self.IDx]
        self.setMinimumSize(QSize(400, 300))
        self.layout = QVBoxLayout()

        self.layout.addWidget(QLabel('What is your Gender?'))

        for answer in range(len(self.answers)):
            self.layout.addWidget(QPushButton(questions[self.IDx][answer]))

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

class PainStartWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.IDx = 'pain_start_question'
        self.answers = questions[self.IDx]
        self.setMinimumSize(QSize(400, 300))
        self.layout = QVBoxLayout()

        self.layout.addWidget(QLabel('When did the pain start?'))

        for answer in range(len(self.answers)):
            self.layout.addWidget(QPushButton(questions[self.IDx][answer]))

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

class PainLocationWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.IDx = 'pain_location_question'
        self.setMinimumSize(QSize(400, 300))
        self.answers = questions[self.IDx]
        self.layout = QVBoxLayout()

        self.layout.addWidget(QLabel('Where is the pain located?'))

        for answer in range(len(self.answers)):
            self.layout.addWidget(QPushButton(questions[self.IDx][answer]))

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

class SwellingLocationWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.IDx = 'swelling_location_question'
        self.answers = questions[self.IDx]
        self.setMinimumSize(QSize(400, 300))
        self.layout = QVBoxLayout()

        self.layout.addWidget(QLabel('Is there swelling of the Knee?'))

        for answer in range(len(self.answers)):
            self.layout.addWidget(QPushButton(questions[self.IDx][answer]))

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

class SwellingWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.IDx = 'swelling_question'
        self.answers = questions[self.IDx]
        self.setMinimumSize(QSize(400, 300))
        self.layout = QVBoxLayout()

        self.layout.addWidget(QLabel('Where is the swelling located?'))

        for answer in range(len(self.answers)):
            self.layout.addWidget(QPushButton(questions[self.IDx][answer]))

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

class BendingWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.IDx = 'bending_question'
        self.answers = questions[self.IDx]
        self.setMinimumSize(QSize(400, 300))
        self.layout = QVBoxLayout()

        self.layout.addWidget(QLabel('Is it painful to bend or extend the knee completely?'))

        for answer in range(len(self.answers)):
            self.layout.addWidget(QPushButton(questions[self.IDx][answer]))

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

class ActivitiesWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.IDx = 'activities_question'
        self.answers = questions[self.IDx]
        self.setMinimumSize(QSize(400, 300))
        self.layout = QVBoxLayout()

        self.layout.addWidget(QLabel('Where is the swelling located?'))

        for answer in range(len(self.answers)):
            self.layout.addWidget(QPushButton(questions[self.IDx][answer]))

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

class ExtensionWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.IDx = 'extension_question'
        self.answers = questions[self.IDx]
        self.setMinimumSize(QSize(400, 300))
        self.layout = QVBoxLayout()

        self.layout.addWidget(QLabel('Where is the swelling located?'))

        for answer in range(len(self.answers)):
            self.layout.addWidget(QPushButton(questions[self.IDx][answer]))

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)


