
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
DB_NAME = "results.db"

@app.route("/", methods=["GET", "POST"])
def home():
    error = None

    if request.method == "POST":
        regno = request.form["regno"]

        con = sqlite3.connect(DB_NAME)
        con.row_factory = sqlite3.Row

        student = con.execute(
            "SELECT * FROM students WHERE regno = ?",
            (regno,)
        ).fetchone()

        con.close()

        if student:
            marks = [
                student["tamil"],
                student["english"],
                student["maths"],
                student["science"],
                student["social"]
            ]

            total = sum(marks)
            percentage = total / 5
            status = (
                "PASS" if all(mark >= 35 for mark in marks)
                else "FAIL"
            )

            return render_template(
                "result.html",
                student=student,
                total=total,
                percentage=percentage,
                status=status
            )

        error = "Register number not found!"

    return render_template("index.html", error=error)

if __name__ == "__main__":
    app.run(debug=True)
