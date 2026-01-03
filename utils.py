# utils.py
# Common helper utilities used across the project

def is_valid_number(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def format_line(text):
    return "-" * len(text)


def safe_input(prompt):
    value = input(prompt).strip()
    while not value:
        print("Input cannot be empty.")
        value = input(prompt).strip()
    return value
