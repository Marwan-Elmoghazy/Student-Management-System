students = []
data_file = "students_data.txt"

LOGIN_USERNAME = "marwan"
LOGIN_PASSWORD = "elmoghazy"


def login():
    max_attempts = 3

    for attempt in range(max_attempts):
        print("\n---- LOGIN ----")
        username = input("Username: ").strip()
        password = input("Password: ")

        if username == LOGIN_USERNAME and password == LOGIN_PASSWORD:
            print("Login successful.\n")
            return True

        attempts_left = max_attempts - attempt - 1
        if attempts_left:
            print(f"Invalid username or password. Attempts left: {attempts_left}")
        else:
            print("Too many failed attempts. Exiting.")
    return False

def initialize_data():
    load_data(True, True)

def load_data(create_if_not_exists=False, finish_message=False):
    students.clear()

    try:
        with open(data_file, "r") as file:
            for line in file:
                student_id, name, age, course, grade = line.strip().split(",")

                students.append(
                    Student(
                        student_id,
                        name,
                        int(age),
                        course,
                        float(grade)
                    )
                )

        if finish_message:
            print(f"Data loaded from {data_file}")
            print(f"Total students: {len(students)}")

    except FileNotFoundError:
        if create_if_not_exists:
            with open(data_file, "w"):
                pass
            print(f"{data_file} not found. Creating a new file.")
        else:
            print(f"{data_file} not found. Starting with an empty list.")

def add_data_to_list(id, name, age, course, degree):
    student = {
        "id": int(id),
        "name": name,
        "age": int(age),
        "course": course,
        "degree": int(degree)
    }

    students.append(student)
    print(f"Added student: {student['id']}, {student['name']}")

def add_data(student):
    with open(data_file, "a") as file:
        file.write(
            f"{student.id},{student.name},{student.age},"
            f"{student.course},{student.grade}\n"
        )
    print(f"Data added to {data_file}")

def clear_file():
    with open(data_file, 'w') as file:
        file.write("")
    print("Data File cleared.")

def clear_data():
    students.clear()
    print("Data cleared from memory.")

def save_all_data(students):
    with open(data_file, "w") as file:
        for student in students:
            file.write(
                f"{student.id},{student.name},{student.age},"
                f"{student.course},{student.grade}\n"
            )


class Student:
    def __init__(self, id, name, age, course, grade):
        self.id = id
        self.name = name
        self.age = age
        self.course = course
        self.grade = grade

    def display_info(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
        print(f"Grade: {self.grade}")

    def get_status(self):
        if self.grade >= 50:
            return "Passed"
        else:
            return "Failed"
        

def add_student(students):
    name = input("Enter student name: ").strip()
    course = input("Enter student course: ").strip()

    try:
        student_id = input("Enter student ID: ").strip()
        age = int(input("Enter student age: "))
        grade = float(input("Enter student grade: "))
    except ValueError:
        print("Invalid input. Please enter valid values.")
        return False

    if not student_id:
        print("Student ID cannot be empty.")
        return False

    if not name or not name.replace(" ", "").isalpha():
        print("Name must contain letters and spaces only.")
        return False

    if not course:
        print("Course cannot be empty.")
        return False

    if age <= 0:
        print("Age must be greater than zero.")
        return False

    if not 0 <= grade <= 100:
        print("Grade must be between 0 and 100.")
        return False

    if search_student_by_id(students, student_id) is not None:
        print("Student already exists.")
        input("Press Enter to return to the menu...")
        return False

    students.append(Student(student_id, name, age, course, grade))
    return True


def search_student_by_id(students, student_id):
    for student in students:
        if student.id == student_id:
            return student
    return None

def search_student_by_name(students, student_name):
    search_results = []
    for student in students:
        if student.name.lower() == student_name.lower():
            search_results.append(student)
    return search_results


def filter_by_course(students, course_name):
    return [
        student for student in students
        if student.course.casefold() == course_name.casefold()
    ]


def show_students(students, title):
    print(f"\n----{title}----\n")
    if not students:
        print("No students found.")
        return

    position = 1
    print("----------------------------")
    for student in students:
        print(f"Rank: {position}")
        student.display_info()
        print("----------------------------")
        position += 1


def show_ranking(students):
    ranked_students = students.copy()

    for i in range(len(ranked_students)):
        for j in range(i + 1, len(ranked_students)):
            if ranked_students[j].grade > ranked_students[i].grade:
                temporary_student = ranked_students[i]
                ranked_students[i] = ranked_students[j]
                ranked_students[j] = temporary_student

    show_students(ranked_students, "STUDENT RANKING")


def update_student_grade(students, student_id):
    student = search_student_by_id(students, student_id)

    if not student:
        print("Student not found.")
        return False

    try:
        new_grade = float(input("Enter new grade: "))
    except ValueError:
        print("Invalid input. Please enter a valid grade.")
        return False

    if not 0 <= new_grade <= 100:
        print("Grade must be between 0 and 100.")
        return False

    student.grade = new_grade
    print("Grade updated successfully.")
    input("Press Enter to return to the menu...")
    return True

def update_student_course(students, student_id):
    student = search_student_by_id(students, student_id)

    if not student:
        print("Student not found.")
        return False

    new_course = input("Enter new course: ").strip()

    if not new_course:
        print("Course cannot be empty.")
        return False

    student.course = new_course
    print("Course updated successfully.")
    input("Press Enter to return to the menu...")
    return True

def update_student_age(students, student_id):
    student = search_student_by_id(students, student_id)

    if not student:
        print("Student not found.")
        return False

    try:
        new_age = int(input("Enter new age: "))
    except ValueError:
        print("Invalid input. Please enter a valid age.")
        return False

    if new_age <= 0:
        print("Age must be greater than zero.")
        return False

    student.age = new_age
    print("Age updated successfully.")
    input("Press Enter to return to the menu...")
    return True

def update_student_name(students, student_id): 
    student = search_student_by_id(students, student_id)

    if not student:
        print("Student not found.")
        return False

    new_name = input("Enter new name: ").strip()

    # Validate that the new name contains only letters and spaces
    if not new_name or not new_name.replace(" ", "").isalpha():
        print("Name must contain letters and spaces only.")
        return False

    student.name = new_name
    print("Name updated successfully.")
    input("Press Enter to return to the menu...")
    return True

def update_student_id(students, student_id):
    student = search_student_by_id(students, student_id)

    if not student:
        print("Student not found.")
        return False

    new_id = input("Enter new ID: ").strip()

    if not new_id:
        print("ID cannot be empty.")
        return False

    existing_student = search_student_by_id(students, new_id)
    if existing_student is not None and existing_student is not student:
        print("A student with this ID already exists.")
        return False

    student.id = new_id
    print("ID updated successfully.")
    input("Press Enter to return to the menu...")
    return True

def update_student(students, student_id):
    student = search_student_by_id(students, student_id)
    #student_by_name = search_student_by_name(students, student_id)

    if not student:
        print("Student not found.")
        return False

    print("\n--- STUDENT UPDATING OPTIONS ---")
    print(f"Updating student: {student.name} (ID: {student.id})")
    print("================================")
    print("1. Update Name")
    print("2. Update Age")
    print("3. Update Course")
    print("4. Update Grade")
    print("5. Update ID")
    print("6. Cancel")
    print("================================")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a valid choice.")
        return False

    if choice == 1:
        return update_student_name(students, student_id)
    elif choice == 2:
        return update_student_age(students, student_id)
    elif choice == 3:
        return update_student_course(students, student_id)
    elif choice == 4:
        return update_student_grade(students, student_id)
    elif choice == 5:
        return update_student_id(students, student_id)
    elif choice == 6:
        print("Update canceled.")
        return False
    else:
        print("Invalid choice.")
        return False

def delete_student(students, student_id):
    student = search_student_by_id(students, student_id)

    if student:
        students.remove(student)
        print("Student deleted successfully.")
        return True

    print("Student not found.")
    return False

def show_statistics(students):
    if not students:
        print("No students available to show statistics.")
        return
    
    total_students = len(students)

    passed = []
    for student in students:
        if student.get_status() == "Passed":
            passed.append(student)
    passed_students = len(passed)

    failed_students = total_students - passed_students

    grades = []
    for student in students:
        grades.append(student.grade)
    total_grade = float(sum(grades))

    average_grade = float(total_grade / total_students)
    
    highest = []
    for student in students:
        highest.append(student.grade)
    highest_grade = float(max(highest))

    print("\n----GLOBAL STATISTICS----")
    print(f"Total Students: {total_students}")
    print(f"Passed Students: {passed_students}")
    print(f"Failed Students: {failed_students}")
    print(f"Average Grade: {average_grade}")
    print(f"Highest Grade: {highest_grade}")
    print("------------------\n")

def get_unique_courses(students):
    unique_courses = set()
    for student in students:
        unique_courses.add(student.course)
    return list(unique_courses)

def get_most_popular_course(students):
    course_count = {}
    student_list = students

    for student in student_list:
        if student.course in course_count:
            course_count[student.course] = course_count[student.course] + 1
        else:
            course_count[student.course] = 1

    return max(course_count, key=course_count.get) if course_count else "There are no courses available."

def course_statistics(students):
    unique_courses = get_unique_courses(students)
    most_popular_course = get_most_popular_course(students)

    print("\n----COURSE STATISTICS----")
    print(f"Available Courses: {', '.join(unique_courses)}")
    print(f"Most Popular Course: {most_popular_course}")
    print("------------------\n")

def main():
    if login() == False:
        return

    initialize_data()
    while True:
        print("\n----STUDENT MANAGEMENT SYSTEM----")
        print("--- BY MARWAN ELMOGHAZY ---")
        print("================================")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Search Student By ID")
        print("4. Search Student By Name")
        print("5. Update Student Data")
        print("6. Delete Student")
        print("7. Show Statistics")
        print("8. Course Statistics")
        print("9. Filter Students By Course")
        print("10. Rank Students By Grade")
        print("11. Exit")
        print("================================")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a valid choice.")
            continue

        if choice == 1:
            if add_student(students):
                save_all_data(students)

        elif choice == 2:
            if not students:
                print("No students available.")
            else:
                print("----------------------------")
                for student in students:
                    student.display_info()
                    print("----------------------------")

            input("Press Enter to return to the menu...")

        elif choice == 3:
            try:
                student_id = input("Enter student ID to search: ").strip()
            except ValueError:
                print("Invalid input. Please enter a valid student ID.")
                continue

            student = search_student_by_id(students, student_id)
            if student:
                print("\n----------------------------")
                student.display_info()
                print("----------------------------\n")
            else:
                print("Student not found.")
            input("Press Enter to return to the menu...")

        elif choice == 4:
            student_name = input("Enter student name to search: ").strip()

            matching_students = search_student_by_name(students, student_name)

            if matching_students:
                for student in matching_students:
                    print("\n----------------------------")
                    student.display_info()
                    print("----------------------------\n")
            else:
                print("Student not found.")
            input("Press Enter to return to the menu...")
            
        elif choice == 5:
            try:
                student_id = input("Enter student ID to update his data: ").strip()
            except ValueError:
                print("Invalid input. Please enter a valid student ID.")
                continue
            if update_student(students, student_id):
                save_all_data(students)

        elif choice == 6:
            try:
                student_id = input("Enter student ID to delete: ").strip()
            except ValueError:
                print("Invalid input. Please enter a valid student ID.")
                continue
            if delete_student(students, student_id):
                save_all_data(students)

        elif choice == 7:
            show_statistics(students)
            input("Press Enter to return to the menu...")

        elif choice == 8:
            course_statistics(students)
            input("Press Enter to return to the menu...")

        elif choice == 9:
            course_name = input("Enter course name to filter: ").strip()
            filtered_students = filter_by_course(students, course_name)
            show_students(filtered_students, f"STUDENTS IN {course_name}")
            input("Press Enter to return to the menu...")

        elif choice == 10:
            show_ranking(students)
            input("Press Enter to return to the menu...")

        elif choice == 11:
            print("Thank you for using the Student Management System by Marwan Elmoghazy. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
            continue

if __name__ == "__main__":
    main()