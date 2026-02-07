from Control.control import Controller
from View.promise_detail_view import PromisedDetail
from View.promise_update_view import PromisedUpdate
from View.politician_view import PoliticianLookup
from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self,userLevel):
        super().__init__()
        self.controller = Controller()
        self.setWindowTitle("Test")
        self.setGeometry(730,300,400,200)
        self.childWindow = None
        self.userLevel = userLevel
        self.memeber = self.showList()
        mainLayout = QVBoxLayout()

        self.mainLabel = QLabel("Click to go to menu")
        self.promisedDetailButton = QPushButton("Promised Detail")
        self.updatePromisedButton = QPushButton("Promised Update")
        self.politicianButton = QPushButton("Politician Lookup")
        self.textBox = QTextEdit(self.memeber)
        self.textBox.setReadOnly(True)

        self.promisedDetailButton.clicked.connect(self.PromisedDetailLauncher)
        self.updatePromisedButton.clicked.connect(self.PromisedUpdateLauncher)
        self.politicianButton.clicked.connect(self.Politicianlookup)

        mainLayout.addWidget(self.mainLabel)

        mainLayout.addWidget(self.promisedDetailButton)
        mainLayout.addWidget(self.updatePromisedButton)
        mainLayout.addWidget(self.politicianButton)
        mainLayout.addWidget(self.textBox)


        self.setLayout(mainLayout)
        self.show()

    def popup(self, text):
        msg = QMessageBox()
        msg.setText(text)
        msg.exec_()

    def PromisedDetailLauncher(self):
        self.childWindow = PromisedDetail(self)
        self.childWindow.show()

    def PromisedUpdateLauncher(self):
        if self.userLevel == 0:
            self.childWindow = PromisedUpdate(self)
            self.childWindow.show()
        else:
            self.popup("you're not allow")

    def Politicianlookup(self):
        self.childWindow = PoliticianLookup(self)
        self.childWindow.show()

    def showList(self):
        result = self.controller.getAllPromised()
        output = ""
        for i in result:
            output += '['
            output += ",".join(map(str,i))
            output += ']'


        return output



# class ShowAllPromised(QWidget):
#     def __init__(self, main):
#         super().__init__ ()
#         self.controller = Controller()
#         self.setWindowTitle("all Promised")
#         self.setGeometry(730,300,400,200)
#
#         promisedLayout = QVBoxLayout()
#
#         self.mainLabel = QLabel("insert text here")
#         self.mainInput = QLineEdit()
#         self.pushButton = QPushButton("test")
#         self.textBox = QTextEdit("Hello there")
#         self.textBox.setReadOnly(True)
#
#         self.pushButton.clicked.connect(lambda: self.testButtonPressed(self.mainInput.text()))
#
#         promisedLayout.addWidget(self.mainLabel)
#         promisedLayout.addWidget(self.mainInput)
#         promisedLayout.addWidget(self.pushButton)
#         promisedLayout.addWidget(self.textBox)
#
#
#         self.setLayout(promisedLayout)
#         self.show()


