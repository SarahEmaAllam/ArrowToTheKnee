from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QStackedWidget
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide2.QtGui import QFont


class IntroductionWindow(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.IDx = 'introduction_question'
        self.start = False
        self.answers = 'intro'
        self.setMinimumSize(QSize(800, 600))
        self.receiver = main_window

        self.layout = QVBoxLayout()

        title = QLabel('Knee Issue Diagnosis')
        font = QFont("Cambria", 30, QFont.Bold)
        title.setFont(font)
        title.setAlignment(Qt.AlignHCenter)
        self.layout.addWidget(title)

        intro = QLabel('An expert knowledge system by team ArrowToTheKnee:\nSarah Allam\nPhil Bischoff\nMikko Brandon')
        font = QFont("Arial", 15, QFont.DemiBold)
        intro.setFont(font)
        intro.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(intro)

        button = QPushButton('Start')
        button.clicked.connect(self.the_button_was_clicked)
        # button.clicked.connect(WindowHandler.showNextScreen)
        self.layout.addWidget(button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    # This function is the same in all other windows, because i just wanted to go through them iteratrively,
    # But here we have the answer which needs to go to the backend, and preferably return a question
    # back to here so we can send it back up to the Window Handler, which finds the corresponding index and
    # displays the question

    def the_button_was_clicked(self):
        print(self.sender().text())
        # self.receiver.recieveAnswer(self.sender().text())
        self.receiver.show_next_screen()
        # send answer to backend#
        # receive new question#

        # send this to the handler with something like self.receiver.showNextScreen(thisquestion)