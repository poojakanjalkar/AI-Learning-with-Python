class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")
        print(f"Marks: {self.marks}")

    def check_pass(self, passing_marks=40):
        if self.marks >= passing_marks:
            print(f"{self.name} has passed the exam.")
        else:
            print(f"{self.name} has failed the exam.")

def main():
    print("Welcome to the Student Management System")
    name = input("Enter the student's name: ")
    roll_no = input("Enter the student's roll number: ")
    try:
        marks = float(input("Enter the student's marks: "))
    except ValueError:
        print("Invalid input for marks. Please enter a number.")
        return

    student = Student(name, roll_no, marks)

    print("\nStudent Details:")
    student.display_details()
    
    print("\nChecking pass/fail status...")
    student.check_pass()

if __name__ == "__main__":
    main()
