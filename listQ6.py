# Program to create a list of students and sort by grade

students = [
    ["Mucyo", 20, "B"],
    ["Muhire", 22, "A"],
    ["Mukiza", 21, "C"],
    ["Mugisha", 19, "A"]
]

students.sort(key=lambda student: student[2])

print("Sorted list of students by grade:")
for student in students:
    print(student)
