import sys
from PySide2.QtWidgets import QApplication, QStackedWidget
from View.MainWindow import MainWindow
from Model.ForwardChaining import *
from Model.Patient import Patient
# from Question_Windows import *
from View.WindowHandler import *
import qdarkstyle
import random
import time




if __name__ == "__main__":

    #var = False

    #dict = [(var, 1)]
    #print(dict)

    #pip install qdarkstyle
    dark_stylesheet = qdarkstyle.load_stylesheet_pyside2()

    app = QApplication(sys.argv)

    #Stylesheets will give a template for different widgets
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    # Main = WindowHandler()
    #
    # #Styling placeholder class
    # intro_Window = IntroductionWindow(Main)
    # age_Window = AgeWindow(Main)
    # gender_Window = GenderWindow(Main)
    # pain_start_Window = PainStartWindow(Main)
    # pain_location_Window = PainLocationWindow(Main)
    # swelling_location_Winow = SwellingLocationWindow(Main)
    # swelling_Window = SwellingWindow(Main)
    # bending_Window = BendingWindow(Main)
    # activity_Window = ActivitiesWindow(Main)
    # extension_Window = ExtensionWindow(Main)
    #
    # stack = QStackedWidget()
    # stack.addWidget(intro_Window)
    # stack.addWidget(age_Window)
    # stack.addWidget(gender_Window)
    # stack.addWidget(pain_start_Window)
    # stack.addWidget(pain_location_Window)
    # stack.addWidget(swelling_location_Winow)
    # stack.addWidget(swelling_Window)
    # stack.addWidget(bending_Window)
    # stack.addWidget(activity_Window)
    # stack.addWidget(extension_Window)
    #
    # Main.addStack(stack)
    #
    # Main.displayWindow()

    main_window = WindowHandler()

    #var = True
    #print(dict)

    kb = KnowledgeBase()
    # Create QuestionHandler that reads all questions from a .txt file
    questions = QuestionsHandler(kb)
    question = questions.questions.pop()

    #window = MainWindow("Knee Issues", questions, question, kb)
    #window.show()

    # First question is popped and sent to view which in turn calls FC when a button is clicked
    patient = Patient()
    #window.update_window(question, patient)

    # Start the event queue (show the first question in the window)
    app.exec_()
