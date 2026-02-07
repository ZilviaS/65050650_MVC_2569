from PyQt5.QtWidgets import *

class PoliticianLookup(QWidget):
    def __init__(self,main):
        super().__init__ ()
        self.main = main
        self.controller = self.main.controller
        self.info = self.lookup()
        self.setWindowTitle("PromisedDetail")
        self.setGeometry(730,300,400,200)
        self.mainLabel = QLabel("politician info")
        promisedLayout = QVBoxLayout()
        self.textBox = QTextEdit(self.info)
        self.textBox.setReadOnly(True)

        promisedLayout.addWidget(self.mainLabel)
        promisedLayout.addWidget(self.textBox)


        self.setLayout(promisedLayout)
        self.show()

    def lookup(self):
        result = self.main.controller.lookup()
        return ",".join(map(str, result))

