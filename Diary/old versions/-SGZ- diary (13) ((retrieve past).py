import sys
import sqlite3
import datetime
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QTextEdit,
    QPushButton, QMessageBox, QLineEdit, QHBoxLayout, QComboBox
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
# Retrieve Window
class RetrieveWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Retrieve Diary Entries")
        self.setGeometry(600, 200, 500, 600)

        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel("Select Entry")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        # --- Dropdown + Button ---
        h_layout = QHBoxLayout()
        self.date_dropdown = QComboBox()
        self.load_entries()   # populate with all entries
        h_layout.addWidget(self.date_dropdown)

        self.confirm_btn = QPushButton("Confirm")
        self.confirm_btn.clicked.connect(self.show_entry)
        h_layout.addWidget(self.confirm_btn)

        layout.addLayout(h_layout)

        # --- Display text area ---
        self.entries_list = QTextEdit()
        self.entries_list.setReadOnly(True)
        layout.addWidget(self.entries_list)

        # Back button
        back_btn = QPushButton("Back to Menu")
        back_btn.clicked.connect(self.back_to_menu)
        layout.addWidget(back_btn)

    def load_entries(self):
        """Load ALL entries (id + date + weekday) into the dropdown"""
        conn = sqlite3.connect("Diary.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, date, weekday FROM entries ORDER BY date DESC, id DESC")
        rows = cursor.fetchall()
        conn.close()

        self.date_dropdown.clear()
        if rows:
            for row in rows:
                entry_id, entry_date, weekday = row
                # Store ID as hidden data
                self.date_dropdown.addItem(f"{entry_date} ({weekday}) - Entry #{entry_id}", entry_id)
        else:
            self.date_dropdown.addItem("No entries found")

    def show_entry(self):
        """Fetch and display entry for the selected id"""
        if self.date_dropdown.currentText() == "No entries found":
            self.entries_list.setText("No entries available.")
            return

        entry_id = self.date_dropdown.currentData()  # get hidden id from dropdown

        conn = sqlite3.connect("Diary.db")
        cursor = conn.cursor()
        cursor.execute("""
            SELECT date, weekday, notes, feelings, reflection, plans, extra 
            FROM entries 
            WHERE id = ?
        """, (entry_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            text = f"Date: {row[0]} ({row[1]})\n"
            text += f"Notes: {row[2]}\n"
            text += f"Feelings: {row[3]}\n"
            text += f"Reflection: {row[4]}\n"
            text += f"Plans: {row[5]}\n"
            text += f"Extra: {row[6]}\n"
            self.entries_list.setText(text)
        else:
            self.entries_list.setText("No entry found.")

    def back_to_menu(self):
        self.menu = MenuWindow()
        self.menu.show()
        self.close()

# ============================================================== 
# Menu Window
class MenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diary Menu")
        self.setGeometry(700, 300, 300, 150)

        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel("What would you like to do?")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        self.new_entry_btn = QPushButton("Add New Entry")
        self.new_entry_btn.clicked.connect(self.open_new_entry)
        layout.addWidget(self.new_entry_btn)

        self.retrieve_btn = QPushButton("Retrieve Entries")
        self.retrieve_btn.clicked.connect(self.open_retrieve_entries)
        layout.addWidget(self.retrieve_btn)

    def open_new_entry(self):
        self.diary_window = DiaryApp()
        self.diary_window.show()
        self.close()

    def open_retrieve_entries(self):
        self.retrieve_window = RetrieveWindow()
        self.retrieve_window.show()
        self.close()

# ============================================================== 
# Login Window
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
            self.open_menu()
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
    
    def open_menu(self):
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

        # Use QTimer to delay opening menu by 1 second
        QTimer.singleShot(1000, self.show_menu_after_welcome)

    def show_menu_after_welcome(self):
        # Close the welcome popup
        self.welcome_popup.close()
        # Open the menu window
        self.menu_window = MenuWindow()
        self.menu_window.show()
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
