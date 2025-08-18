from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt, QTimer
from MenuWindow import MenuWindow
from PasswordManager import PasswordManager

class LoginWindow(QWidget):
    def __init__(self, db):
        super().__init__()
        self.setWindowTitle("Diary Login")
        self.setGeometry(800, 400, 300, 50)

        self.tries_left = 3
        self.db = db

        # Password manager
        self.pwm = PasswordManager()
        self.pwm.set_password("Password123")  # Set once

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel("Enter Password:")
        layout.addWidget(self.label)

        h_layout = QHBoxLayout()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        h_layout.addWidget(self.password_input)

        self.eye_button = QPushButton("👁")
        self.eye_button.setCheckable(True)
        self.eye_button.setFixedWidth(30)
        self.eye_button.clicked.connect(self.toggle_password)
        h_layout.addWidget(self.eye_button)

        layout.addLayout(h_layout)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.check_password)
        layout.addWidget(self.login_button)

    def toggle_password(self):
        if self.eye_button.isChecked():
            self.password_input.setEchoMode(QLineEdit.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.Password)

    def check_password(self):
        password = self.password_input.text()
        if self.pwm.verify_password(password):
            self.open_menu()
        else:
            self.tries_left -= 1
            if self.tries_left > 0:
                self.show_popup(f"Invalid password. {self.tries_left} tries left.", color="yellow")
                self.password_input.clear()
            else:
                self.show_popup("Too many failed attempts. Exiting.", color="red", duration=1500)
                QTimer.singleShot(1500, self.close)

    def show_popup(self, message, color="lightgreen", duration=1000):
        popup = QLabel(message, self)
        popup.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint)
        popup.setStyleSheet(f"background-color: {color}; padding: 15px; border: 1px solid black; font-size: 16px;")
        popup.adjustSize()
        parent_center = self.geometry().center()
        popup_rect = popup.frameGeometry()
        popup_rect.moveCenter(parent_center)
        popup.move(popup_rect.topLeft())
        popup.show()
        QTimer.singleShot(duration, popup.close)

    def open_menu(self):
        # Show welcome popup first
        self.welcome_popup = QLabel("Welcome!", self)
        self.welcome_popup.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint)
        self.welcome_popup.setStyleSheet(
            "background-color: lightgreen; padding: 15px; border: 1px solid black; font-size: 16px;"
        )
        self.welcome_popup.adjustSize()
        parent_center = self.geometry().center()
        popup_rect = self.welcome_popup.frameGeometry()
        popup_rect.moveCenter(parent_center)
        self.welcome_popup.move(popup_rect.topLeft())
        self.welcome_popup.show()

        # After 1 second, close popup and open menu
        QTimer.singleShot(1000, self.show_menu_after_welcome)

    def show_menu_after_welcome(self):
        self.welcome_popup.close()
        from MenuWindow import MenuWindow  # safe to import again
        self.menu_window = MenuWindow(self.db)
        self.menu_window.show()
        self.close()

