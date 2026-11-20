# Name: CADORNA, JAY-R RAMOS
# Section: IV-BSIT __A
# Activity: P1 - Student Grade Calculator
# Date: 2026-11-20

def divide_numbers():
    try:
        first = float(input("First number: "))
        second = float(input("Second number: "))
        result = first / second
    except ValueError:
        print("Invalid number. Please enter numeric values.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print("Result:", result)
    finally:
        print("Division operation finished.")

def read_file():
    filename = input("Enter file name: ").strip()
    try:
        with open(filename, "r", encoding="utf-8") as file:
            contents = file.read()
    except FileNotFoundError:
        print("The requested file does not exist.")
    except PermissionError:
        print("You do not have permission to read that file.")
    else:
        print("--- FILE CONTENTS ---")
        print(contents)
    finally:
        print("File operation finished.")

def main():
    while True:
        print("=== SAFE MENU PROGRAM ===")
        print("1. Divide two numbers")
        print("2. Open and read a text file")
        print("3. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            divide_numbers()
        elif choice == "2":
            read_file()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid menu selection. Choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
