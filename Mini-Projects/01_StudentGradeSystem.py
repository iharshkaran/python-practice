# Problem:
# Write a program to process the marks of multiple students.
# • First, ask the user how many students are there.
# • For each student, input their marks.
# • Assign grades based on the following conditions:
# o Marks ≥ 90 → Grade A
# o Marks ≥ 75 → Grade B
# o Marks ≥ 50 → Grade C
# o Marks < 50 → Fail
# • Display the grade for each student.
# • Finally, calculate and display the average marks of the class.

num_students = int(input("Enter number of students: "))
total = 0

for i in range(1, num_students + 1):
    marks = int(input(f"Enter marks for student {i}: "))
    total += marks

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"

    print(f"Student {i} Grade: {grade}")

average = total / num_students
print(f"\nClass Average Marks: {average}")