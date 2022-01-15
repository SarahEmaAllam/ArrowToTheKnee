import sys
from KnowledgeBase import *
from View.WindowHandler import *
import qdarkstyle


if __name__ == "__main__":

    dark_stylesheet = qdarkstyle.load_stylesheet_pyside2()

    app = QApplication(sys.argv)

    # Stylesheets will give a template for different widgets
    app.setStyleSheet(qdarkstyle.load_stylesheet())

    kb = KnowledgeBase()
    main_window = WindowHandler(kb)

    # Start the event queue (show the introduction window)
    app.exec_()
