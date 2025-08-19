from PyQt5.QtWidgets import QApplication
from LoginWindow import LoginWindow
from Database import Database
import sys

if __name__ == "__main__":
    db = Database()
    app = QApplication(sys.argv)
    login = LoginWindow(db)
    login.show()
    sys.exit(app.exec_())
