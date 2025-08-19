import sys
import sqlite3
import datetime
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QTextEdit,
    QPushButton, QMessageBox, QLineEdit, QBoxLayout
)
from PyQt5.QtCore import Qt, QTimer

# ==============================================================
# Database Setup
def init_db():
    conn = sqlite3.connect("Diary.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            weekday TEXT,
            notes TEXT,
            feelings TEXT,
            reflection TEXT,
            plans TEXT,
            extra TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_entry(entry):
    conn = sqlite3.connect("Diary.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO entries (date, weekday, notes, feelings, reflection, plans, extra)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, entry)
    conn.commit()
    conn.close()

# ==============================================================
# Diary Window
class DiaryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Diary")
        self.setGeometry(600, 200, 700, 800)

        # Main container
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Date + Weekday
        dateNow = datetime.datetime.now()
        self.userDate = dateNow.strftime('%Y-%m-%d')
        self.weekday = dateNow.strftime('%A')

        layout.addWidget(QLabel(f"Date: {self.userDate}"))
        layout.addWidget(QLabel(f"Weekday: {self.weekday}"))

        # --- Notes ---
        layout.addWidget(QLabel("Notes: Brief summary of what happened today."))
        self.notes_text = QTextEdit()
        layout.addWidget(self.notes_text)

        # --- Feelings ---
        layout.addWidget(QLabel("Feelings: Thoughts and feelings about today's events."))
        helper = QLabel(
            "- How did you feel?\n"
            "- What you're worried/happy/proud about?\n"
            "- Any emotional release (venting)?"
        )
        helper.setStyleSheet("color: gray; font-size: 11px;")
        layout.addWidget(helper)
        self.feelings_text = QTextEdit()
        layout.addWidget(self.feelings_text)

        # --- Reflection ---
        layout.addWidget(QLabel("Reflection: Reflection on today's events."))
        helper = QLabel(
            "- Lessons learnt from the day.\n"
            "- Things you'd do differently.\n"
            "- Gratitude note (what you're thankful for)."
        )
        helper.setStyleSheet("color: gray; font-size: 11px;")
        layout.addWidget(helper)
        self.reflection_text = QTextEdit()
        layout.addWidget(self.reflection_text)

        # --- Plans ---
        layout.addWidget(QLabel("Plans: Plans and goals for tomorrow."))
        helper = QLabel(
            "- What you want to achieve tomorrow/future.\n"
            "- Tasks or events to prepare for.\n"
            "- Goals (short-term or long-term)."
        )
        helper.setStyleSheet("color: gray; font-size: 11px;")
        layout.addWidget(helper)
        self.plans_text = QTextEdit()
        layout.addWidget(self.plans_text)

        # --- Extra ---
        layout.addWidget(QLabel("Extra Notes: Any other thoughts."))
        helper = QLabel(
            "- Anything that doesn’t fit in other sections.\n"
            "- Random thoughts, ideas, or observations.\n"
            "- Quotes, jokes, or anything interesting."
        )
        helper.setStyleSheet("color: gray; font-size: 11px;")
        layout.addWidget(helper)
        self.extra_text = QTextEdit()
        layout.addWidget(self.extra_text)

        # --- Buttons ---
        self.save_button = QPushButton("Save Entry")
        self.save_button.clicked.connect(self.save_entry_to_db)
        layout.addWidget(self.save_button)

        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(self.close)
        layout.addWidget(self.exit_button)

    def save_entry_to_db(self):
        entry = (
            self.userDate,
            self.weekday,
            self.notes_text.toPlainText(),
            self.feelings_text.toPlainText(),
            self.reflection_text.toPlainText(),
            self.plans_text.toPlainText(),
            self.extra_text.toPlainText()
        )
        save_entry(entry)
        QMessageBox.information(self, "Saved", "Your diary entry was saved successfully!")

# ==============================================================
# Login Window
from PyQt5.QtWidgets import QHBoxLayout

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diary Login")
        self.setGeometry(800, 400, 300, 50)

        self.tries_left = 3
        self.valid_pw = "Password123"

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel("Enter Password:")
        layout.addWidget(self.label)

        # --- HORIZONTAL LAYOUT for password + eye ---
        h_layout = QHBoxLayout()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        h_layout.addWidget(self.password_input)

        self.eye_button = QPushButton("👁")  # eye icon
        self.eye_button.setCheckable(True)
        self.eye_button.setFixedWidth(30)
        self.eye_button.clicked.connect(self.toggle_password)
        h_layout.addWidget(self.eye_button)

        layout.addLayout(h_layout)  # add horizontal layout to main layout

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.check_password)
        layout.addWidget(self.login_button)

    # --- toggle password function ---
    def toggle_password(self):
        if self.eye_button.isChecked():
            self.password_input.setEchoMode(QLineEdit.Normal)  # show password
        else:
            self.password_input.setEchoMode(QLineEdit.Password)  # hide password

    def check_password(self):
        password = self.password_input.text()
        if password == self.valid_pw:
            self.open_diary()
        else:
            self.tries_left -= 1
            if self.tries_left > 0:
                self.show_popup(
                    f"Invalid password. {self.tries_left} tries left.",
                    color="yellow"
                )
                self.password_input.clear()
            else:
                self.show_popup(
                    "Too many failed attempts. Exiting.",
                    color="red",
                    duration=1500  # a little longer before closing
                )
                QTimer.singleShot(1500, self.close)  # close window after showing popup

    # --- Popup function for messages ---
    def show_popup(self, message, color="lightgreen", duration=1000):
        popup = QLabel(message, self)
        popup.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint)
        popup.setStyleSheet(
            f"background-color: {color}; padding: 15px; border: 1px solid black; font-size: 16px;"
        )
        popup.adjustSize()
        # Center popup on login window
        parent_center = self.geometry().center()
        popup_rect = popup.frameGeometry()
        popup_rect.moveCenter(parent_center)
        popup.move(popup_rect.topLeft())
        popup.show()
        QTimer.singleShot(duration, popup.close)  # auto-close after duration
    
    def open_diary(self):
        # --- Welcome popup ---
        self.welcome_popup = QLabel("Welcome!", self)
        self.welcome_popup.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint)
        self.welcome_popup.setStyleSheet(
            "background-color: lightgreen; padding: 15px; border: 1px solid black; font-size: 16px;"
        )
        self.welcome_popup.adjustSize()
        # Center popup on login window
        parent_center = self.geometry().center()
        popup_rect = self.welcome_popup.frameGeometry()
        popup_rect.moveCenter(parent_center)
        self.welcome_popup.move(popup_rect.topLeft())
        self.welcome_popup.show()

        # Use QTimer to delay opening diary by 1 second
        QTimer.singleShot(1000, self.show_diary_after_welcome)

    def show_diary_after_welcome(self):
        # Close the welcome popup
        self.welcome_popup.close()
        # Open the diary window
        self.diary_window = DiaryApp()
        self.diary_window.show()
        # Close login window
        self.close()

# ==============================================================
# Main
if __name__ == "__main__":
    init_db()
    app = QApplication(sys.argv)
    login = LoginWindow()
    login.show()
    sys.exit(app.exec_())
