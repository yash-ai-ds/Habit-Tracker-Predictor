import sqlite3
from datetime import date

DB_NAME = "habits.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def initialize_database():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS habits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                created_at DATE NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS completions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                habit_id INTEGER NOT NULL,
                completion_date DATE NOT NULL,
                FOREIGN KEY (habit_id) REFERENCES habits (id),
                UNIQUE(habit_id, completion_date)
            )
        ''')
        conn.commit()

def add_habit(name):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO habits (name, created_at) VALUES (?, ?)', (name, date.today().isoformat()))
            conn.commit()
            return True
    except sqlite3.IntegrityError:
        return False

def get_habits():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, created_at FROM habits')
        return cursor.fetchall()
        
def mark_completion(habit_id, completion_date=None):
    if not completion_date:
        completion_date = date.today().isoformat()
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO completions (habit_id, completion_date) VALUES (?, ?)', (habit_id, completion_date))
            conn.commit()
            return True
    except sqlite3.IntegrityError:
        return False

def get_completions(habit_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT completion_date FROM completions WHERE habit_id = ? ORDER BY completion_date ASC', (habit_id,))
        return [row[0] for row in cursor.fetchall()]
        
def get_habit_by_id(habit_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, created_at FROM habits WHERE id = ?', (habit_id,))
        return cursor.fetchone()
