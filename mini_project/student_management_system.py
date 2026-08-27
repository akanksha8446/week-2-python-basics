students = []
def add_student():
    roll_number = input("Enter roll number: ")
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    student = {
        "roll_number": roll_number,
        "name": name,
        "marks": marks
    }
    students.append(student)
    print("Student added successfully!")
def view_students():
    if not students:
        print("\nNo student records found.")
        return
    print("\n----- Student Records -----")
    for student in students:
        print(
            f"Roll No: {student['roll_number']} | "
            f"Name: {student['name']} | "
            f"Marks: {student['marks']}"
        )
def search_student():
    roll_number = input("Enter roll number to search: ")
    for student in students:
        if student["roll_number"] == roll_number:
            print("\nStudent Found!")
            print("Roll Number:", student["roll_number"])
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            return
    print("Student not found.")
def delete_student():
    roll_number = input("Enter roll number to delete: ")
    for student in students:
        if student["roll_number"] == roll_number:
            students.remove(student)
            print("Student deleted successfully!")
            return
    print("Student not found.")
while True:
    print("\n==============================")
    print("   STUDENT MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    print("==============================")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("\nThank you for using Student Management System!")
        break
    else:
        print("Invalid choice! Please try again.")
