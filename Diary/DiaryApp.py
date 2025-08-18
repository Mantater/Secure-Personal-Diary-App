import datetime
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QMessageBox
)
import Database as db

class DiaryApp(QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.setWindowTitle("My Diary")
        self.setGeometry(600, 200, 700, 800)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Date and Weekday
        dateNow = datetime.datetime.now()
        self.userDate = dateNow.strftime('%Y-%m-%d')
        self.weekday = dateNow.strftime('%A')
        layout.addWidget(QLabel(f"Date: {self.userDate}"))
        layout.addWidget(QLabel(f"Weekday: {self.weekday}"))

        # Sections
        self.notes_text = self.create_section(layout, "Notes", "Brief summary of what happened today.")
        self.feelings_text = self.create_section(layout, "Feelings", 
            "- How did you feel?\n- What you're worried/happy/proud about?\n- Any emotional release (venting)?")
        self.reflection_text = self.create_section(layout, "Reflection", 
            "- Lessons learnt from the day.\n- Things you'd do differently.\n- Gratitude note (what you're thankful for).")
        self.plans_text = self.create_section(layout, "Plans", 
            "- What you want to achieve tomorrow/future.\n- Tasks or events to prepare for.\n- Goals (short-term or long-term).")
        self.extra_text = self.create_section(layout, "Extra Notes", 
            "- Anything that doesn’t fit in other sections.\n- Random thoughts, ideas, or observations.\n- Quotes, jokes, or anything interesting.")

        # Buttons
        self.save_button = QPushButton("Save Entry")
        self.save_button.clicked.connect(self.save_entry_to_db)
        layout.addWidget(self.save_button)

        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(self.close)
        layout.addWidget(self.exit_button)

    def create_section(self, layout, title, helper_text=""):
        layout.addWidget(QLabel(f"{title}:"))
        if helper_text:
            helper = QLabel(helper_text)
            helper.setStyleSheet("color: gray; font-size: 11px;")
            layout.addWidget(helper)
        text_edit = QTextEdit()
        layout.addWidget(text_edit)
        return text_edit

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
        self.db.save_entry(entry)
        QMessageBox.information(self, "Saved", "Your diary entry was saved successfully!")
