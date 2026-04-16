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
        
        db.cursor.execute("SELECT * FROM exercises WHERE name = (?)", (name,))
        if db.cursor.fetchone():
            db.cursor.execute("UPDATE exercises SET weight = (?), reps = (?), adjustment_lvl = (?) WHERE name = (?)", 
                              (weight, reps, adjustment_lvl, name))
        else:
            db.cursor.execute("INSERT INTO exercises (workout_id, name, weight, reps, adjustment_lvl) VALUES (?, ?, ?, ?, ?)", 
                            (workout_id, name, weight, reps, adjustment_lvl))
        db.conn.commit()
    
    @staticmethod
    def get_exercises(db):
        db.cursor.execute("SELECT * FROM exercises")
        return db.cursor.fetchall()

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
            weight REAL NOT NULL,
            reps INTEGER NOT NULL,
            adjustment_lvl INTEGER,
            FOREIGN KEY (workout_id) REFERENCES workouts(id)
        )        
    """)
    db.conn.commit()
    print("tables created")
    
def add_exercise(db, workout_id, name, weight, reps, adjustment_lvl=None):
    db.cursor.execute("SELECT * FROM workouts WHERE id = ?", (workout_id,))
    if not db.cursor.fetchone():
        print("ERROR: Workout doesnt exist")
        Workout.add_workout(db, datetime.date.today())
        print("New workout added")
        
    Exercise.add_exercise(db, workout_id, name, weight, reps, adjustment_lvl)
    print(f"exercise added to workout {workout_id}")
        

if __name__ == "__main__":
    db = Database("data.db")
    create_tables(db)
    
    Workout.add_workout(db, datetime.date.today())
    add_exercise(db, 2, "bench_press", 60, 8)
    print("Exercises", Exercise.get_exercises(db))
    print("Workouts", Workout.get_workouts(db))