# Program to store and calculate the total marks of students in different subjects
marks = []

num_students = int(input("Enter the number of students: "))
num_subjects = int(input("Enter the number of subjects: "))

for i in range(num_students):
    student_marks = []
    print(f"\nEnter marks for Student {i + 1}:")
    for j in range(num_subjects):
        mark = float(input(f"Subject {j + 1} marks: "))
        student_marks.append(mark)
    marks.append(student_marks)

print("\nTotal marks of students:")
for i in range(num_students):
    total = sum(marks[i])
    print(f"Student {i + 1}: Total Marks = {total}")
