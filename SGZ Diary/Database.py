import sqlite3

class Database:
    def __init__(self, db_name="Diary.db"):
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_name)
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

    def save_entry(self, entry):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO entries (date, weekday, notes, feelings, reflection, plans, extra)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, entry)
        conn.commit()
        conn.close()

    def get_entries(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT id, date, weekday FROM entries ORDER BY date DESC, id DESC")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_entry_by_id(self, entry_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT date, weekday, notes, feelings, reflection, plans, extra
            FROM entries WHERE id = ?
        """, (entry_id,))
        row = cursor.fetchone()
        conn.close()
        return row
