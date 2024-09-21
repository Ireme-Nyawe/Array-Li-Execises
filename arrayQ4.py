# Program to reverse the order of student marks in a subject

marks = []
subject=input("Enter subject: ")

num_students = int(input("Enter the number of students: "))
print("Enter the marks for each student:")
for i in range(num_students):
    marks.append(float(input(f"Mark for student {i+1}: ")))

marks.reverse()

print(f"\nReversed order of student {subject} marks:")
print(marks)
