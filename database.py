import sqlite3

class Database:
    def __init__(self, db_name='signals.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_signals_table()

    def create_signals_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS signals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            signal TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )''')
        self.connection.commit()

    def insert_signal(self, signal):
        self.cursor.execute('INSERT INTO signals (signal) VALUES (?)', (signal,))
        self.connection.commit()

    def get_signals(self):
        self.cursor.execute('SELECT * FROM signals')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()

# Example usage:
# db = Database()
# db.insert_signal('Buy signal for BTC')
# print(db.get_signals())
# db.close()