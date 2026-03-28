students = {}

def add_student():
    while True:
        try:
            student_id = int(input("Student's ID: "))
            if student_id in students:
                print("Student already exists\n")
                continue
            else:
                student_name = input("Student's Name: ")
                students[student_id] = {"name": student_name}
                print("Student Added!\n")
                break
        except ValueError:
            print("Invalid Input\n")


def add_major():
    if not students:
        print("No students added!\n")
    else:
        while True:
            try:
                student_id = int(input("Student's ID: "))
                if student_id not in students:
                    print("Student does not exist\n")
                    continue
                else:
                    student_major = input("Student's Major: ")
                    students[student_id]["major"] = student_major
                    print("Major Added!\n")
                    break
            except ValueError:
                print("Invalid Input\n")


def view_all_students():
    if not students:
        print("No students added!\n")
    else:
        for key in students:
            name = students[key].get("name", "N/A")
            major = students[key].get("major", "N/A")
            print(f"ID: {key:<5} Name: {name:<15} Major: {major}")
        print()


def search_for_student():
    if not students:
        print("No students added!\n")
    else:
        try:
            student_id = int(input("Student's ID: "))
            if student_id in students:
                print("Student Found!")
                print(f"ID: {student_id}")
                print(f"Name: {students[student_id].get('name', 'N/A')}")
                print(f"Major: {students[student_id].get('major', 'N/A')}\n")
            else:
                print("Student not found!\n")
        except ValueError:
            print("Invalid Input!\n")


def update_student():
    if not students:
        print("No students added!\n")
    else:
        print("Update feature coming soon...\n")


def delete_student():
    if not students:
        print("No students added!\n")
    else:
        print("Delete feature coming soon...\n")


if __name__ == "__main__":
    print("---- Student Management System Started ----")
    while True:
        print("1. Add a student")
        print("2. Add student major")
        print("3. View all students")
        print("4. Search for student")
        print("5. Update a student")
        print("6. Delete a student")
        print("7. Exit")

        try:
            choice = int(input("Choice: "))
            match choice:
                case 1:
                    add_student()
                case 2:
                    add_major()
                case 3:
                    view_all_students()
                case 4:
                    search_for_student()
                case 5:
                    update_student()
                case 6:
                    delete_student()
                case 7:
                    break
                case _:
                    print("Invalid Choice!\n")
        except ValueError:
            print("Invalid Input!\n")