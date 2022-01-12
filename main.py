import sys
from PySide2.QtWidgets import QApplication, QStackedWidget
from View.MainWindow import MainWindow
from Model.ForwardChaining import *
from Model.Patient import Patient
from Question_Windows import *
import qdarkstyle




if __name__ == "__main__":

    #var = False

    #dict = [(var, 1)]
    #print(dict)

    #pip install qdarkstyle
    dark_stylesheet = qdarkstyle.load_stylesheet_pyside2()

    app = QApplication(sys.argv)

    #Stylesheets will give a template for different widgets
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    #Styling placeholder class
    intro_Window = IntroductionWindow()

    #Trying some stuff here
    intro_Window = IntroductionWindow()
    main_Window = WindowHandler(intro_Window)
    main_Window.makeWindow()
    activity_window = ActivitiesWindow()
    main_Window.changeWindow(activity_window)
    main_Window.makeWindow()

    #Stack to store Questions

    #stack = QStackedWidget()
    #stack.addWidget(intro_window)

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
