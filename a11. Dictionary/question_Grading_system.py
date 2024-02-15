Student_marks = {'amrjeet': 92, 'vanshaj': 91, 'shivika': 98, 'ayesha': 87, 'sheetal': 91, 'sonu': 88, 'khalid': 87}
Student_grades = {}

for mark in Student_marks:
    marks = Student_marks[mark]
    if marks > 90:
        Student_grades[mark] = 'A+'
    elif marks > 80:
        Student_grades[mark] = 'A'
    elif marks > 70:
        Student_grades[mark] = 'B+'
    elif marks > 60:
        Student_grades[mark] = 'B'
    elif marks > 50:
        Student_grades[mark] = 'C'
    elif marks > 40:
        Student_grades[mark] = 'D'
    else:
        Student_grades[mark] = 'F'

print(Student_grades)
