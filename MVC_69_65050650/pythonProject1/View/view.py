from PyQt5.QtCore import QLine

from Control.control import Controller
from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__ ()
        self.controller = Controller()
        self.setWindowTitle("Test")
        self.setGeometry(730,300,400,200)
        self.childWindow = None

        mainLayout = QVBoxLayout()

        self.mainLabel = QLabel("Click to go to menu")
        self.promisedDetailButton = QPushButton("Promised Detail")
        self.updatePromisedButton = QPushButton("Promised Update")
        self.pushButton = QPushButton("test")
        self.textBox = QTextEdit("Hello there")
        self.textBox.setReadOnly(True)

        self.promisedDetailButton.clicked.connect(self.PromisedDetailLauncher)
        self.pushButton.clicked.connect(lambda: self.testButtonPressed(self.mainInput.text()))

        mainLayout.addWidget(self.mainLabel)

        mainLayout.addWidget(self.promisedDetailButton)
        mainLayout.addWidget(self.pushButton)
        mainLayout.addWidget(self.textBox)


        self.setLayout(mainLayout)
        self.show()

    def testButtonPressed(self,text):
        self.textBox.setPlainText(self.controller.test(text))

    def PromisedDetailLauncher(self):
        self.childWindow = PromisedDetail(self)
        self.childWindow.show()


class ShowAllPromised(QWidget):
    def __init__(self, main):
        super().__init__ ()
        self.controller = Controller()
        self.setWindowTitle("all Promised")
        self.setGeometry(730,300,400,200)

        promisedLayout = QVBoxLayout()

        self.mainLabel = QLabel("insert text here")
        self.mainInput = QLineEdit()
        self.pushButton = QPushButton("test")
        self.textBox = QTextEdit("Hello there")
        self.textBox.setReadOnly(True)

        self.pushButton.clicked.connect(lambda: self.testButtonPressed(self.mainInput.text()))

        promisedLayout.addWidget(self.mainLabel)
        promisedLayout.addWidget(self.mainInput)
        promisedLayout.addWidget(self.pushButton)
        promisedLayout.addWidget(self.textBox)


        self.setLayout(promisedLayout)
        self.show()

class PromisedDetail(QWidget):
    def __init__(self, main):
        super().__init__ ()
        self.controller = Controller()
        self.setWindowTitle("PromisedDetail")
        self.setGeometry(730,300,400,200)

        promisedLayout = QVBoxLayout()

        self.mainLabel = QLabel("insert text here")
        self.mainInput = QLineEdit()
        self.pushButton = QPushButton("test")
        self.textBox = QTextEdit("Hello there")
        self.textBox.setReadOnly(True)

        self.pushButton.clicked.connect(lambda: self.testButtonPressed(self.mainInput.text()))

        promisedLayout.addWidget(self.mainLabel)
        promisedLayout.addWidget(self.mainInput)
        promisedLayout.addWidget(self.pushButton)
        promisedLayout.addWidget(self.textBox)


        self.setLayout(promisedLayout)
        self.show()

