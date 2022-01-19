from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QLabel, QVBoxLayout, QWidget
from PySide2.QtWidgets import QMainWindow, QPushButton, QSizePolicy
from PySide2.QtGui import QFont, QPixmap


# Subclass of QMainWindow to customize the application's introduction window
class IntroductionWindow(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        # Standard window settings
        self.setMinimumSize(QSize(1000, 600))
        self.layout = QVBoxLayout()

        self.IDx = 'introduction_question'
        self.start = False
        self.answers = 'intro'
        self.receiver = main_window

        title = QLabel('Knee Issue Diagnosis')
        font = QFont("Cambria", 30, QFont.Bold)
        title.setFont(font)
        title.setAlignment(Qt.AlignHCenter)
        self.layout.addWidget(title)

        #Adding picture
        label = QLabel(self)
        pixmap = QPixmap('View/logo.png')
        label.setScaledContents(True)
        label.setPixmap(pixmap)
        label.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        label.setFixedWidth(500)
        label.setFixedHeight(500)
        self.layout.addWidget(label, alignment=Qt.AlignCenter)

        intro = QLabel('An expert knowledge system by:\nSarah Allam\nPhil Bischoff\nMikko Brandon')
        font = QFont("Arial", 15, QFont.DemiBold)
        intro.setFont(font)
        intro.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(intro)

        button = QPushButton('Start')
        button.clicked.connect(self.the_button_was_clicked)
        self.layout.addWidget(button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    # Function defining button behavior when clicked
    def the_button_was_clicked(self):
        self.receiver.show_next_screen()
