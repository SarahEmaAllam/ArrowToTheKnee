import sys
from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QStackedWidget
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

#Class that handles the windows
class WindowHandler:
    def __init__(self):

        self.stack = []

        #I'm sure this is how professionals debug as well!
        print("SHIT")

    def addStack(self, stack):
        self.stack = stack

    def displayWindow(self):
        self.stack.show()

    #Not Done
    def receive_question(self, question):
        question = matchQuestionToWindow(question)
        print(type(question))
        print("question is", question)
        self.changeWindow(question)
        self.window.show()

    #I dont know either
    def receiveAnswer(self, Answer):
        print( Answer )

    #This function is called from the specific windows. Because it only increases the index, we get 
    #the pages iteratively (self.stack.currentIndex() + 1) We still need to do something where we have some question:index data
    #structure and we get the index and then the question that the backend wants us to show, then we just use the index
    #as an argument and then we can display any question window
    def showNextScreen(self):
        print(self.stack.currentIndex())
        self.stack.setCurrentIndex(self.stack.currentIndex() + 1)
        self.displayWindow()


class IntroductionWindow(QMainWindow,):
        def __init__(self, Main):
            super().__init__()
            self.IDx = 'introduction_question'
            self.start = False
            self.answers = 'intro'
            self.setMinimumSize(QSize(400, 300))
            self.receiver = Main

            self.layout = QVBoxLayout()

            self.layout.addWidget(QLabel('Did you recently take an arrow to the knee?'))

            button = QPushButton('Yes please help')
            button.setCheckable(True)
            button.clicked.connect(self.the_button_was_clicked)
            #button.clicked.connect(WindowHandler.showNextScreen)
            button = self.layout.addWidget(button)

            container = QWidget()
            container.setLayout(self.layout)
            self.setCentralWidget(container)


        #This function is the same in all other windows, because i just wanted to go through them iteratrively,
        #But here we have the answer which needs to go to the backend, and preferably return a question
        #back to here so we can send it back up to the Window Handler, which finds the corresponding index and
        #displays the question

        def the_button_was_clicked(self):
            print(self.sender().text())
            #self.receiver.recieveAnswer(self.sender().text())
            self.receiver.showNextScreen()
            #send answer to backend#
            #receive new question#

            #send this to the handler with something like self.receiver.showNextScreen(thisquestion)

#All other Windows, essentially the same
class AgeWindow(QMainWindow):
    def __init__(self, Main):
        super().__init__()
        self.IDx = 'age_question'
        self.answers = questions[self.IDx]
        self.setMinimumSize(QSize(400, 300))
        self.receiver = Main

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
        print(self.sender().text())
        #WindowHandler.recieveAnswer(self.sender().text())
        self.receiver.showNextScreen()

class GenderWindow(QMainWindow):
    def __init__(self, Main):
        super().__init__()

        self.IDx = 'gender_question'
        self.answers = questions[self.IDx]
        self.setMinimumSize(QSize(400, 300))
        self.layout = QVBoxLayout()
        self.receiver = Main

        self.layout.addWidget(QLabel('What is your Gender?'))

        for answer in range(len(self.answers)):
            button = QPushButton(questions[self.IDx][answer])
            button.setCheckable(True)
            button.clicked.connect(self.the_button_was_clicked)
            button = self.layout.addWidget(button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def the_button_was_clicked(self):
        print(self.sender().text())
        #WindowHandler.recieveAnswer(self.sender().text())
        self.receiver.showNextScreen()

class PainStartWindow(QMainWindow):
    def __init__(self, Main):
        super().__init__()

        self.IDx = 'pain_start_question'
        self.answers = questions[self.IDx]
        self.setMinimumSize(QSize(400, 300))
        self.layout = QVBoxLayout()
        self.receiver = Main

        self.layout.addWidget(QLabel('When did the pain start?'))

        for answer in range(len(self.answers)):
            button = QPushButton(questions[self.IDx][answer])
            button.setCheckable(True)
            button.clicked.connect(self.the_button_was_clicked)
            button = self.layout.addWidget(button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def the_button_was_clicked(self):
        print(self.sender().text())
        #WindowHandler.recieveAnswer(self.sender().text())
        self.receiver.showNextScreen()

class PainLocationWindow(QMainWindow):
    def __init__(self, Main):
        super().__init__()

        self.IDx = 'pain_location_question'
        self.setMinimumSize(QSize(400, 300))
        self.answers = questions[self.IDx]
        self.layout = QVBoxLayout()
        self.receiver = Main

        self.layout.addWidget(QLabel('Where is the pain located?'))

        for answer in range(len(self.answers)):
            button = QPushButton(questions[self.IDx][answer])
            button.setCheckable(True)
            button.clicked.connect(self.the_button_was_clicked)
            button = self.layout.addWidget(button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
    
    def the_button_was_clicked(self):
        print(self.sender().text())
        #WindowHandler.recieveAnswer(self.sender().text())
        self.receiver.showNextScreen()

class SwellingLocationWindow(QMainWindow):
    
    def __init__(self, Main):
        super().__init__()

        self.IDx = 'swelling_location_question'
        self.answers = questions[self.IDx]
        self.setMinimumSize(QSize(400, 300))
        self.layout = QVBoxLayout()
        self.receiver = Main

        self.layout.addWidget(QLabel('Is there swelling of the Knee?'))

        for answer in range(len(self.answers)):
            button = QPushButton(questions[self.IDx][answer])
            button.setCheckable(True)
            button.clicked.connect(self.the_button_was_clicked)
            button = self.layout.addWidget(button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
        
    def the_button_was_clicked(self):
        print(self.sender().text())
        #WindowHandler.recieveAnswer(self.sender().text())
        self.receiver.showNextScreen()

class SwellingWindow(QMainWindow):
    
    def __init__(self, Main):
        super().__init__()

        self.IDx = 'swelling_question'
        self.answers = questions[self.IDx]
        self.setMinimumSize(QSize(400, 300))
        self.layout = QVBoxLayout()
        self.receiver = Main

        self.layout.addWidget(QLabel('Where is the swelling located?'))

        for answer in range(len(self.answers)):
            button = QPushButton(questions[self.IDx][answer])
            button.setCheckable(True)
            button.clicked.connect(self.the_button_was_clicked)
            button = self.layout.addWidget(button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def the_button_was_clicked(self):
        print(self.sender().text())
        #WindowHandler.recieveAnswer(self.sender().text())
        self.receiver.showNextScreen()

class BendingWindow(QMainWindow):
    def __init__(self, Main):
        super().__init__()

        self.IDx = 'bending_question'
        self.answers = questions[self.IDx]
        self.setMinimumSize(QSize(400, 300))
        self.layout = QVBoxLayout()
        self.receiver = Main

        self.layout.addWidget(QLabel('Is it painful to bend or extend the knee completely?'))

        for answer in range(len(self.answers)):
            button = QPushButton(questions[self.IDx][answer])
            button.setCheckable(True)
            button.clicked.connect(self.the_button_was_clicked)
            button = self.layout.addWidget(button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
        
    def the_button_was_clicked(self):
        print(self.sender().text())
        #WindowHandler.recieveAnswer(self.sender().text())
        self.receiver.showNextScreen()

class ActivitiesWindow(QMainWindow):
    def __init__(self, Main):
        super().__init__()

        self.IDx = 'activities_question'
        self.answers = questions[self.IDx]
        self.setMinimumSize(QSize(400, 300))
        self.layout = QVBoxLayout()
        self.receiver = Main

        self.layout.addWidget(QLabel('Where is the swelling located?'))

        for answer in range(len(self.answers)):
            button = QPushButton(questions[self.IDx][answer])
            button.setCheckable(True)
            button.clicked.connect(self.the_button_was_clicked)
            button = self.layout.addWidget(button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def the_button_was_clicked(self):
        print(self.sender().text())
        #WindowHandler.recieveAnswer(self.sender().text())
        self.receiver.showNextScreen()

class ExtensionWindow(QMainWindow):
    def __init__(self, Main):
        super().__init__()

        self.IDx = 'extension_question'
        self.answers = questions[self.IDx]
        self.setMinimumSize(QSize(400, 300))
        self.layout = QVBoxLayout()
        self.receiver = Main

        self.layout.addWidget(QLabel('Where is the swelling located?'))

        for answer in range(len(self.answers)):
            button = QPushButton(questions[self.IDx][answer])
            button.setCheckable(True)
            button.clicked.connect(self.the_button_was_clicked)
            button = self.layout.addWidget(button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def the_button_was_clicked(self):
        print(self.sender().text())
        #WindowHandler.recieveAnswer(self.sender().text())
        self.receiver.showNextScreen()
