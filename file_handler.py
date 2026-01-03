# file_handler.py
# Handles saving, loading, and searching student result records

FILE_PATH = "data/students.txt"


def save_result(result):
    record = (
        f"{result['roll_no']},"
        f"{result['name']},"
        f"{result['total']},"
        f"{result['percentage']},"
        f"{result['grade']}\n"
    )

    with open(FILE_PATH, "a") as file:
        file.write(record)


def load_all_results():
    try:
        with open(FILE_PATH, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []


def roll_number_exists(roll_no):
    records = load_all_results()
    for record in records:
        stored_roll = record.split(",")[0]
        if stored_roll == roll_no:
            return True
    return False


def search_by_roll(roll_no):
    records = load_all_results()
    for record in records:
        stored_roll = record.split(",")[0]
        if stored_roll == roll_no:
            return record.strip()
    return None
