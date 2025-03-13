import sqlite3

class Database:
    def __init__(self, db_name):
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fname TEXT,
            lname TEXT,
            email TEXT,
            password TEXT)
        ''')
        self.con.commit()

    def insert(self, fname, lname, email, password):
        self.cur.execute("INSERT INTO users (fname, lname, email, password) VALUES (?, ?, ?, ?)",
                            (fname, lname, email, password))
        self.con.commit()

    def find_user(self, email, password):
        self.cur.execute("SELECT fname, lname FROM users WHERE email = ? AND password = ?", (email, password))
        return self.cur.fetchone()

