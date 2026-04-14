import sqlite3
import datetime

class Database:
    def __init__(self, file_path):
        self.conn = sqlite3.connect(file_path)
        self.cursor = self.conn.cursor()

class Workout:
    @staticmethod
    def add_workout(db, date):
        try:
            db.cursor.execute("INSERT INTO workouts (date) VALUES (?)", (str(date),))
            db.conn.commit()
            print("workout added")
        except sqlite3.IntegrityError:
            print("ERROR: workout already exists for this date")
            
    @staticmethod
    def get_workouts(db):
        db.cursor.execute("SELECT * FROM workouts")
        return db.cursor.fetchall()
    
class Exercise:
    @staticmethod
    def add_exercise(db, workout_id, name, weight, reps, adjustment_lvl=None):
        pass
    


def create_tables(db):
    db.cursor.execute("""
        CREATE TABLE IF NOT EXISTS workouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL UNIQUE
        )        
    """)
    db.cursor.execute("""
        CREATE TABLE IF NOT EXISTS exercises (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            workout_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            weight INTEGER NOT NULL,
            reps INTEGER NOT NULL,
            adjustment_lvl INTEGER,
            FOREIGN KEY (workout_id) REFERENCES workouts(id)
        )        
    """)
    db.conn.commit()
    print("tables created")

if __name__ == "__main__":
    db = Database("data.db")
    create_tables(db)
    Workout.add_workout(db, datetime.date.today())
    print(Workout.get_workouts(db))