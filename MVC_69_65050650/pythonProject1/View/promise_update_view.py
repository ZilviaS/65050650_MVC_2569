from PyQt5.QtCore import QLine

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QLocale

class PromisedUpdate(QWidget):
    def __init__(self, main):
        super().__init__ ()
        self.main = main
        self.controller = self.main.controller
        self.setWindowTitle("PromisedUpdate")
        self.setGeometry(730,300,400,200)

        promisedLayout = QVBoxLayout()

        self.IDLabel = QLabel("insert promised ID here")
        self.IDInput = QLineEdit()
        self.dateInput = QDateEdit()
        self.dateInput.setLocale(QLocale(QLocale.English))
        self.dateInput.setDisplayFormat("yyyy-MM-dd")
        self.DetailLabel = QLabel("insert Detail:")
        self.DetailInput = QLineEdit()
        self.pushButton = QPushButton("submit")
        self.textBox = QTextEdit("Hello there")
        self.textBox.setReadOnly(True)

        self.pushButton.clicked.connect(self.updatePromised)

        promisedLayout.addWidget(self.IDLabel)
        promisedLayout.addWidget(self.IDInput)
        promisedLayout.addWidget(self.dateInput)
        promisedLayout.addWidget(self.DetailLabel)
        promisedLayout.addWidget(self.DetailInput)
        promisedLayout.addWidget(self.pushButton)
        promisedLayout.addWidget(self.textBox)



        self.setLayout(promisedLayout)
        self.show()

    def updatePromised(self):
        thai_digits = "๐๑๒๓๔๕๖๗๘๙"
        eng_digits = "0123456789"
        trans_table = str.maketrans(thai_digits, eng_digits)

        # print(self.dateInput.date().toString("yyyy-MM-dd").translate(trans_table))

        result =  self.main.controller.updatePromised([self.IDInput.text(),self.dateInput.date().toString("yyyy-MM-dd").translate(trans_table),self.DetailInput.text()])
        self.textBox.setPlainText(result)