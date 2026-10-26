
import sqlite3

DB_NAME = "results.db"

def create_database():
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            regno INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            tamil INTEGER,
            english INTEGER,
            maths INTEGER,
            science INTEGER,
            social INTEGER
        )
    """)

    students = [
        (1001, "Arun", 85, 78, 92, 88, 80),
        (1002, "Priya", 90, 86, 95, 91, 89),
        (1003, "Kumar", 65, 70, 58, 72, 68),
        (1004, "Divya", 45, 55, 62, 50, 60),
        (1005, "Suresh", 30, 40, 35, 42, 38)
    ]

    cur.executemany("""
        INSERT OR IGNORE INTO students
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, students)

    con.commit()
    con.close()

    print("Database created successfully!")
    print("Five student records are ready.")

if __name__ == "__main__":
    create_database()
