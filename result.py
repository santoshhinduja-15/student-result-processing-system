# result.py
# Handles result calculation and grading logic

def generate_result(student):
    marks = student["marks"]
    total_marks = sum(marks)
    subject_count = len(marks)
    percentage = total_marks / subject_count

    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "Fail"

    result = {
        "roll_no": student["roll_no"],
        "name": student["name"],
        "total": total_marks,
        "percentage": round(percentage, 2),
        "grade": grade
    }

    return result
