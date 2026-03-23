students = {}

def add_student():
    while True:
        try:
            student_id = int(input("Student's ID: "))
            if student_id in students:
                print("Student already exists")
                continue
            else:
                key = student_id
                student_name = input("Student's Name: ").title().strip()
                first = student_name
                last = student_name
                value = student_name
                students[key] = value
                break
        except ValueError:
            print("Invalid Input")


def view_all_students():
    if not students:
        print("No students added!\n")
    else:
        print()

def search_for_student():
    if not students:
        print("No students added!\n")
    else:
        students_id = int(input("Student's ID: "))
        if students_id in students:
            print("Student Found!\n")
        else:
            print("Student not found!\n")
    pass

def update_student():
    if not students:
        print("No students added!\n")
    else:
        print()
    pass

def delete_student():
    if not students:
        print("No students added!\n")
    else:
        print()

if __name__ == "__main__":
    print("---- Student Management System Started ----")
    while True:
        print("1. Add a student")
        print("2. View all students")
        print("3. Search for student")
        print("4. Update a student")
        print("5. Delete a student")
        print("6. Exit")
        try:
            choice = int(input("Choice: "))
            match choice:
                case 1:
                    add_student()
                case 2:
                    view_all_students()
                case 3:
                    search_for_student()
                case 4:
                    update_student()
                case 5:
                    delete_student()
                case 6:
                    break
                case _:
                    print("Invalid Choice!\n")
        except ValueError:
            print("Invalid Input!\n")


