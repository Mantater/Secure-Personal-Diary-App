import sys
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QComboBox,
    QPushButton, QTextEdit, QHBoxLayout
)
from PyQt5.QtCore import Qt

class RetrieveWindow(QWidget):
    def __init__(self, db):
        super().__init__()
        self.db = db
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
        rows = self.db.get_entries() 

        self.date_dropdown.clear()
        if rows:
            for row in rows:
                entry_id, entry_date, weekday = row
                
                self.date_dropdown.addItem(
                    f"{entry_date} ({weekday}) - Entry #{entry_id}", entry_id
                )
        else:
            self.date_dropdown.addItem("No entries found")

    def show_entry(self):
        """Fetch and display entry for the selected id"""
        if self.date_dropdown.currentText() == "No entries found":
            self.entries_list.setText("No entries available.")
            return

        entry_id = self.date_dropdown.currentData()
        row = self.db.get_entry_by_id(entry_id)

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
        from MenuWindow import MenuWindow
        self.menu = MenuWindow(self.db)
        self.menu.show()
        self.close()
