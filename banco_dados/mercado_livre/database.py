import sqlite3

class Database:
    def __init__(self, nome):
        self.conn = sqlite3.connect(nome)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.commit()
        self.conn.close()