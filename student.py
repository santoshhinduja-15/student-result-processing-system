# student.py
# Handles student information input and validation

from file_handler import roll_number_exists


def create_student():
    student = {}

    while True:
        roll_no = input("Enter Roll Number: ").strip()
        if roll_number_exists(roll_no):
            print("Roll number already exists. Enter a different roll number.")
        else:
            student["roll_no"] = roll_no
            break

    student["name"] = input("Enter Student Name: ").strip()

    marks = []
    subject_count = int(input("Enter number of subjects: "))

    for i in range(subject_count):
        while True:
            try:
                mark = int(input(f"Enter marks for subject {i + 1}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks should be between 0 and 100.")
            except ValueError:
                print("Please enter valid numeric marks.")

    student["marks"] = marks
    return student
