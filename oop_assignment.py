class Student:
    def __init__(self, name, student_id, email, age, department, marks=None):
        self.name = name
        self.student_id = student_id
        self.__email = email   
        self.age = age
        self.department = department
        self.__marks = marks if marks is not None else []

    # Getter
    def get_email(self):
        return self.__email

    # Setter
    def set_email(self, email):
        self.__email = email

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Email: {self.__email}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")

    # Method Overloading using *args 
    def calculate_result(self, *args):
        if args:
            self.__marks = list(args)
        if not self.__marks:
            return "No marks available."
        average = sum(self.__marks) / len(self.__marks)
        return f"Average Marks: {average:.2f}"

    def get_student_type(self):
        return "General Student"


class UndergraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, semester, marks=None):
        super().__init__(name, student_id, email, age, department, marks)
        self.semester = semester

    # Method Overriding
    def get_student_type(self):
        return "Undergraduate Student"

    def display_info(self):
        super().display_info()
        print(f"Semester: {self.semester}")


class GraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, research_topic, marks=None):
        super().__init__(name, student_id, email, age, department, marks)
        self.research_topic = research_topic

    # Method Overriding
    def get_student_type(self):
        return "Graduate Student"

    def display_info(self):
        super().display_info()
        print(f"Research Topic: {self.research_topic}")


print("--- Undergraduate Student Record ---")
ug_student = UndergraduateStudent("Atonu","UG-01", "atonu@example.com", 21, "Computer", "6th" )
ug_student.display_info()
print(f"Student Type: {ug_student.get_student_type()}")
print(ug_student.calculate_result(85, 90, 78, 88)) 



print("\n--- Graduate Student Record ---")
grad_student = GraduateStudent("Prottoy", "GR-02", "prottoy@example.com", 24, "Civil", "Sustainable Infrastructure Design")
grad_student.display_info()
print(f"Student Type: {grad_student.get_student_type()}")
print(grad_student.calculate_result(92, 88, 95)) 



print("\n--- Polymorphism Implementation ---")
all_students = [ug_student, grad_student]
for student in all_students:
	print(f"{student.name} is classified as a {student.get_student_type()}.")
