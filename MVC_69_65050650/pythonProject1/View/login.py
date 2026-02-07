from PyQt5.QtWidgets import *
from Control.control import Controller
from View.promise_list_view import MainWindow


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(730, 300, 400, 200)
        loginLayout = QVBoxLayout()

        self.mainWindow = None
        self.controller = Controller()

        self.userNameLabel = QLabel("Insert User Name")
        self.userNameInput = QLineEdit()
        self.passLabel = QLabel("Insert Password")
        self.passInput = QLineEdit()
        self.loginButton = QPushButton("Login")

        self.loginButton.clicked.connect(self.Authentication)

        loginLayout.addWidget(self.userNameLabel)
        loginLayout.addWidget(self.userNameInput)
        loginLayout.addWidget(self.passLabel)
        loginLayout.addWidget(self.passInput)
        loginLayout.addWidget(self.loginButton)

        self.setLayout(loginLayout)

        self.show()

    def Authentication(self):
        result = self.controller.authentication(self.userNameInput.text(),self.passInput.text())
        if result == 1 or result == 0:
            self.mainWindow = MainWindow(result)
        else:
            self.popup()

    def popup(self):
        msg = QMessageBox()
        msg.setText("Error you are not in the system")
        msg.exec_()
