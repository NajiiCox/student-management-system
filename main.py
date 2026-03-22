students = {}

def add_student():
    student_id = int(input("Student's ID: "))
    key = student_id
    student_name = input("Student's Name: ")
    value = student_name
    students[key] = value

def view_all_students():
    pass

def search_for_student():
    pass

def update_student():
    pass

def delete_student():
    pass

if __name__ == "__main__":
    while True:
        print("---- Student Management System Started ----")
        print("1. Add a student")
        print("2. View all students")
        print("3. Search for student")
        print("4. Update a student")
        print("5. Delete a student")
        print("6. Exit")
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

