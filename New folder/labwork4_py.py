

import os
import zipfile
import json

# Create folders
os.makedirs("pw5/domains", exist_ok=True)

# ---------------- student.py ----------------
with open("pw5/domains/student.py", "w") as f:
    f.write('''
class Student:
    def __init__(self, name, marks, credits):
        self.name = name
        self.marks = marks
        self.credits = credits

    def calculate_gpa(self):
        return sum(m*c for m, c in zip(self.marks, self.credits)) / sum(self.credits)
''')

open("pw5/domains/__init__.py", "w").close()

# ---------------- input.py ----------------
with open("pw5/input.py", "w") as f:
    f.write('''
from domains.student import Student

def get_students():
    students = [
        Student("John", [8, 7, 9], [3, 3, 2]),
        Student("Alice", [7, 8, 8], [3, 2, 3]),
        Student("Peter", [9, 8, 7], [2, 3, 3])
    ]

    with open("students.txt", "w") as f:
        for s in students:
            f.write(s.name + "\\n")

    with open("marks.txt", "w") as f:
        for s in students:
            f.write(str(s.marks) + "\\n")

    courses = ["Mathematics", "Programming", "Computer Architecture"]

    with open("courses.txt", "w") as f:
        for c in courses:
            f.write(c + "\\n")

    return students
''')

# ---------------- output.py ----------------
with open("pw5/output.py", "w") as f:
    f.write('''
def show_students(students):
    students.sort(key=lambda x: x.calculate_gpa(), reverse=True)

    for s in students:
        print(s.name, "GPA =", round(s.calculate_gpa(), 2))
''')

# ---------------- main.py ----------------
with open("pw5/main.py", "w") as f:
    f.write('''
import os
import zipfile
from input import get_students
from output import show_students

# Load old data if students.dat exists
if os.path.exists("students.dat"):
    print("Loading saved data...")
    with zipfile.ZipFile("students.dat", "r") as z:
        z.extractall(".")
else:
    students = get_students()

    # Compress all files into students.dat
    with zipfile.ZipFile("students.dat", "w") as z:
        z.write("students.txt")
        z.write("courses.txt")
        z.write("marks.txt")

    print("New data saved.")

show_students(students)
''')

# Run the program
os.chdir("pw5")
!python main.py