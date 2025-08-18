from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from DiaryApp import DiaryApp
from RetrieveWindow import RetrieveWindow

class MenuWindow(QWidget):
    def __init__(self, db):
        super().__init__()
        self.db = db
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
        self.diary_window = DiaryApp(self.db)
        self.diary_window.show()
        self.close()

    def open_retrieve_entries(self):
        self.retrieve_window = RetrieveWindow(self.db)
        self.retrieve_window.show()
        self.close()
