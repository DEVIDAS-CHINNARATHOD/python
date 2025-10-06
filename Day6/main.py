# Mini Student Management System
students = {
    1: {"name": "Pavan Kalyan", "course": "CSE", "marks": 88},
    2: {"name": "Gurukiran", "course": "ECE", "marks": 91},
    3: {"name": "Harsha", "course": "ME", "marks": 75},
}

def show_students():
    print("\nStudent List:")
    for id, info in students.items():
        print(f"ID: {id} | Name: {info['name']} | Course: {info['course']} | Marks: {info['marks']}")

def add_student():
    sid = len(students) + 1
    name = input("Enter student name: ")
    course = input("Enter course: ")
    marks = int(input("Enter marks: "))
    students[sid] = {"name": name, "course": course, "marks": marks}
    print(f"\nAdded {name} successfully!")

def delete_student():
    sid = int(input("Enter student ID to delete: "))
    if sid in students:
        removed = students.pop(sid)
        print(f"Removed student: {removed['name']}")
    else:
        print(" No student found with that ID.")

def find_topper():
    topper = max(students.values(), key=lambda x: x["marks"])
    print(f"\nTopper: {topper['name']} ({topper['marks']} marks)")

def average_marks():
    total = sum(s["marks"] for s in students.values())
    avg = total / len(students)
    print(f"\nAverage Marks: {avg:.2f}")

def main():
    while True:
        print("\n===== clear" \
        "Student Management Menu =====")
        print("1. Show Students")
        print("2. Add Student")
        print("3. Delete Student")
        print("4. Find Topper")
        print("5. Average Marks")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_students()
        elif choice == "2":
            add_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            find_topper()
        elif choice == "5":
            average_marks()
        elif choice == "6":
            print(" Exiting... Have a great day!")
            break
        else:
            print(" Invalid choice! Try again.")

if __name__ == "__main__":
    main()
