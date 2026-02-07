from PyQt5.QtWidgets import *

class PromisedDetail(QWidget):
    def __init__(self,main):
        super().__init__ ()
        self.main = main
        self.controller = self.main.controller
        self.setWindowTitle("PromisedDetail")
        self.setGeometry(730,300,400,200)

        promisedLayout = QVBoxLayout()

        self.mainLabel = QLabel("insert Promised ID")
        self.mainInput = QLineEdit()
        self.pushButton = QPushButton("enter")
        self.textBox = QTextEdit("waiting for enter")
        self.textBox.setReadOnly(True)

        self.pushButton.clicked.connect(self.search)

        promisedLayout.addWidget(self.mainLabel)
        promisedLayout.addWidget(self.mainInput)
        promisedLayout.addWidget(self.pushButton)
        promisedLayout.addWidget(self.textBox)


        self.setLayout(promisedLayout)
        self.show()

    def search(self):
        result = self.main.controller.searchPromisedDetail(self.mainInput.text())
        print(result)
        if result[0] == 0:
            self.textBox.setText(result[1])
        else:
            self.textBox.setText(",".join(map(str, result[1])))