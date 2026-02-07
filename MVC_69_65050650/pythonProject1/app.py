import sys
from PyQt5.QtWidgets import QApplication
from View.login import LoginWindow

if __name__ == "__main__":
    app = QApplication([])
    window = LoginWindow()
    sys.exit(app.exec_())
