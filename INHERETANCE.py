class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def enroll_course(self, course_name):
        print(f"{self.name} has successfully enrolled in {course_name}.")

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")


class Lecturer(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def teach_course(self, course_name):
        print(f"Dr./Prof. {self.name} is teaching {course_name}.")


student = Student("Mashud", 22, "FOE.41.006.157.25")
lecturer = Lecturer("Matthew", 35, "LEC.456")

print("--- Testing Student Class ---")
student.display_info()
student.enroll_course("Electrical Engineering")

print("\n--- Testing Lecturer Class ---")
lecturer.display_info()
lecturer.teach_course("OOP")