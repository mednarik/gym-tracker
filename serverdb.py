import sqlite3
import datetime

conn = sqlite3.connect("gym.db")
cursor = conn.cursor()

def create_tables():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS workouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL
        )        
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS exercises (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            workout_id INTEGER NOT NULL,
            FOREIGN KEY (workout_id) REFERENCES workouts(id)
        )        
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            reps INTEGER NOT NULL,
            weight REAL NOT NULL,
            exercise_id INTEGER NOT NULL,
            FOREIGN KEY (exercise_id) REFERENCES exercises(id)
        )        
    """)
    conn.commit()

def add_exercise():
    datetime.date.today()


if __name__ == "__main__":
    print(datetime.date.today())