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
        db.cursor.execute("SELECT weight, reps FROM exercises WHERE workout_id = (?) AND name = (?)", (workout_id, name))
        row = db.cursor.fetchone()
        if row:
            if weight > row[0] or reps > row[1]:
                db.cursor.execute("UPDATE exercises SET weight = (?), reps = (?), adjustment_lvl = (?) WHERE name = (?) AND workout_id = (?)", 
                                (weight, reps, adjustment_lvl, name, workout_id))
                print("updated exercises stats")
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
    print("tables created maybe")
    
def add_exercise(db, name, weight, reps, adjustment_lvl=None) -> None:
    today = str(datetime.date.today())

    db.cursor.execute("SELECT MAX(id) FROM workouts")
    last_id = db.cursor.fetchone()[0]
    if last_id is None:
        Workout.add_workout(db, today)
        Exercise.add_exercise(db, 1, name, weight, reps, adjustment_lvl)
        print(f"exercise added to workout {1}")
        return
        
    db.cursor.execute("SELECT date FROM workouts WHERE id = ?", (last_id,))
    date = db.cursor.fetchone()[0]
    if date != today:
        Workout.add_workout(db, today)
        Exercise.add_exercise(db, last_id + 1, name, weight, reps, adjustment_lvl)
        print(f"exercise added to workout {last_id + 1}")
        return
    
    Exercise.add_exercise(db, last_id, name, weight, reps, adjustment_lvl)
    print(f"exercise added to workout {last_id}")
        

if __name__ == "__main__":
    db = Database("data.db")
    create_tables(db)
    
    add_exercise(db, "bench_press", 60, 10)
    print("Exercises", Exercise.get_exercises(db))
    print("Workouts", Workout.get_workouts(db))