class Student:
    school_name = "Arya College"   # Class Variable

    def __init__(self, name, student_class, roll, marks):
        self.name = name
        self.student_class = student_class
        self.roll = roll
        self.marks = marks   # list of marks for 5 subjects

    def calculate_grade(self):
        avg = sum(self.marks) / len(self.marks)
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 40:
            return "D"
        else:
            return "F"

    def display(self):
        print("\n--- Student Details ---")
        print(f"Name: {self.name}")
        print(f"Class: {self.student_class}")
        print(f"Roll No: {self.roll}")
        print(f"Marks: {self.marks}")
        print(f"Average: {sum(self.marks)/len(self.marks):.2f}")
        print(f"Grade: {self.calculate_grade()}")
        print(f"School: {Student.school_name}")


# Taking input from user
name = input("Enter student name: ")
student_class = input("Enter class: ")
roll = int(input("Enter roll number: "))

marks = []
for i in range(5):
    m = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

# Create object and display details
s1 = Student(name, student_class, roll, marks)
s1.display()
