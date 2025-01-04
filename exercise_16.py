class Student:
    def __init__(self, student_id, name, age, room_number, contact):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.room_number = room_number
        self.contact = contact


class HostelManagement:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age, room_number, contact):
        if student_id in self.students:
            print("Student with this ID already exists!")
        else:
            new_student = Student(student_id, name, age, room_number, contact)
            self.students[student_id] = new_student
            print(f"Student {name} added successfully!")

    def view_students(self):
        if not self.students:
            print("No students in the hostel!")
        else:
            print("\n--- List of Students ---")
            for student_id, student in self.students.items():
                print(f"ID: {student.student_id}, Name: {student.name}, Age: {student.age}, "
                      f"Room: {student.room_number}, Contact: {student.contact}")

    def update_student(self, student_id):
        if student_id not in self.students:
            print("Student not found!")
        else:
            print("\n--- Update Student Details ---")
            student = self.students[student_id]
            student.name = input("Enter new name: ") or student.name
            student.age = int(input("Enter new age: ") or student.age)
            student.room_number = input("Enter new room number: ") or student.room_number
            student.contact = input("Enter new contact: ") or student.contact
            print(f"Student {student.name}'s details updated successfully!")

    def delete_student(self, student_id):
        if student_id not in self.students:
            print("Student not found!")
        else:
            removed_student = self.students.pop(student_id)
            print(f"Student {removed_student.name} removed successfully!")



def main():
    hostel = HostelManagement()
    while True:
        print("\n--- Hostel Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            room_number = input("Enter room number: ")
            contact = input("Enter contact number: ")
            hostel.add_student(student_id, name, age, room_number, contact)
        elif choice == '2':
            hostel.view_students()
        elif choice == '3':
            student_id = input("Enter student ID to update: ")
            hostel.update_student(student_id)
        elif choice == '4':
            student_id = input("Enter student ID to delete: ")
            hostel.delete_student(student_id)
        elif choice == '5':
            print("Exiting Hostel Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
