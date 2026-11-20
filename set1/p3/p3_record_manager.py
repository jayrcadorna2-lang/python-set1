
students = []


# 1. ADD STUDENT
def add_student():
    print("\n=== ADD STUDENT ===")

    student_id = input("Enter Student ID: ").strip()

    # Check if Student ID already exists
    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Student Name: ").strip()
    age = input("Enter Student Age: ").strip()
    course = input("Enter Student Course: ").strip()

    if not student_id or not name or not age or not course:
        print("All fields are required!")
        return

    students.append({
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    })

    print("\nStudent added successfully!")


# 2. REMOVE STUDENT
def remove_student():
    print("\n=== REMOVE STUDENT ===")

    student_id = input("Enter Student ID to remove: ").strip()

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student removed successfully!")
            return

    print("Student not found!")


# 3. SEARCH STUDENT
def search_student():
    print("\n=== SEARCH STUDENT ===")

    student_id = input("Enter Student ID to search: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("\n=== STUDENT FOUND ===")
            print("Student ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            return

    print("Student not found!")


# 4. DISPLAY ALL STUDENTS

# 4. DISPLAY ALL STUDENTS
def display_students():
    print("\n=== ALL STUDENT RECORDS ===")

    if len(students) == 0:
        print("No student records available.")
        return

    print("\n{:<15} {:<20} {:<10} {:<15}".format(
        "STUDENT ID", "NAME", "AGE", "COURSE"
    ))

    print("-" * 65)

    for student in students:
        print("{:<15} {:<20} {:<10} {:<15}".format(
            student["id"],
            student["name"],
            student["age"],
            student["course"]
        ))

    print("-" * 65)
    print("Total Students:", len(students))


# 5. MAIN MENU
def main():
    while True:
        print("\n=== STUDENT RECORD MANAGER ===")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            remove_student()

        elif choice == "3":
            search_student()

        elif choice == "4":
            display_students()

        elif choice == "5":
            print("\nThank you for using Student Record Manager!")
            print("Goodbye!")
            break

        else:
            print("\nInvalid menu selection!")
            print("Please choose from 1 to 5.")


# RUN PROGRAM
if __name__ == "__main__":
    main()
