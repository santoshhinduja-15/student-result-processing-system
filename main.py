# main.py
# Entry point of Student Result Processing System

from student import create_student
from result import generate_result
from file_handler import save_result, load_all_results, search_by_roll


def show_menu():
    print("\n====== Student Result Processing System ======")
    print("1. Add New Student Result")
    print("2. View All Results")
    print("3. Search Student by Roll Number")
    print("4. Exit")


def add_student():
    student_data = create_student()
    result_data = generate_result(student_data)
    save_result(result_data)
    print("\nResult saved successfully.")


def view_results():
    results = load_all_results()
    if not results:
        print("\nNo records found.")
    else:
        print("\n----- Stored Student Results -----")
        for record in results:
            print(record.strip())


def search_student():
    roll_no = input("Enter Roll Number to search: ").strip()
    record = search_by_roll(roll_no)

    if record:
        print("\nStudent Record Found:")
        print(record)
    else:
        print("\nNo student found with this roll number.")


while True:
    show_menu()
    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        view_results()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("\nExiting system. Goodbye.")
        break
    else:
        print("\nInvalid choice. Please select 1 to 4.")
