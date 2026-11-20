# Name: CADORNA, JAY-R RAMOS
# Section: IV-BSIT __A
# Activity: P1 - Student Grade Calculator
# Date: 2026-11-20

import student_utils
from student_utils import calculate_average
from datetime import datetime

def main():
    grades = []
    print("Enter grades from 0 to 100. Type 'done' when finished.")
    while True:
        raw = input("Grade: ").strip()
        if raw.lower() == "done":
            break
        try:
            grade = float(raw)
            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Grade must be from 0 to 100.")
        except ValueError:
            print("Please enter a number.")

    if not grades:
        print("No grades entered.")
        return

    print("\\n=== GRADE REPORT ===")
    print("Generated:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print(f"Average: {calculate_average(grades):.2f}")  # from module import name
    print(f"Highest: {student_utils.get_highest(grades)}")  # import module
    print(f"Lowest: {student_utils.get_lowest(grades)}")
    print(f"Status: {student_utils.check_status(grades)}")

if __name__ == "__main__":
    main()
