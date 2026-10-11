student = {}

while True:
    print("\n----- Student Management App -----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Check Result")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")
 # Add Student
    if choice == '1':
        name = input("Enter student name: ")
        roll_number = input("Enter roll number: ")
        marks = float(input("Enter marks: "))
        student[roll_number] = {'name': name, 'marks': marks}
        print(f"Student {name} added successfully.")
# View Students
    elif choice == '2':
        if not student:
            print("No students found.")
        else:
            print("\n----- Student List -----")
            for roll_number, details in student.items():
                print(f"Roll Number: {roll_number}, Name: {details['name']}, Marks: {details['marks']}")
# Check Result
    elif choice == '3':
        roll_number = input("Enter roll number to check result: ")
        if roll_number in student:
            print(f"Roll Number: {roll_number}")
            print(f"Name: {student[roll_number]['name']}")
            print(f"Marks: {student[roll_number]['marks']}")

            if student[roll_number]['marks'] >= 40:
                print("Result: Pass")
            else:
                print("Result: Fail")
        else:
            print("Student not found.")
# Exit
    elif choice == '4':
        print("Exiting the app. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")