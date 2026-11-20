
def enter_grades():
    grades = []
    while True:
        raw = input("Enter a grade (or type 'done'): ").strip()
        if raw.lower() == "done":
            break
        try:
            grade = float(raw)
            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Grade must be from 0 to 100.")
        except ValueError:
            print("Please enter a valid number.")
    if not grades:
        print("No grades were entered.")
    return grades

def calculate_total(grades):
    return sum(grades)

def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0

def get_highest(grades):
    return max(grades) if grades else None

def get_lowest(grades):
    return min(grades) if grades else None

def check_status(grades):
    return "PASSED" if grades and calculate_average(grades) >= 75 else "FAILED"

def main():
    grades = []
    while True:
        print("=== STUDENT GRADE CALCULATOR ===")
        print("1. Enter grades")
        print("2. View results")
        print("3. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            grades = enter_grades()
        elif choice == "2":
            if not grades:
                print("Please enter grades first.")
            else:
                print(f"Total Grades: {calculate_total(grades):.2f}")
                print(f"Average: {calculate_average(grades):.2f}")
                print(f"Highest: {get_highest(grades):.2f}")
                print(f"Lowest: {get_lowest(grades):.2f}")
                print(f"Status: {check_status(grades)}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid menu choice.")

if __name__ == "__main__":
    main()
