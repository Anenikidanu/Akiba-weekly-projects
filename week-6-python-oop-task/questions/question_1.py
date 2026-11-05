class Student:
    def __init__(self, name, student_id, department):
        self.name=name
        self.student_id=student_id
        self.department=department
    def  display_info(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Department: {self.department}")
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am a student in the {self.department} department.")

student1 = Student("Ani", "ETS001", "Software Engineering")
student2 = Student("Abel", "ETS002", "Electrical Engineering")
student3 = Student("Sara", "ETS003", "Civil Engineering")

student1.display_info()
student1.introduce()

student2.display_info()
student2.introduce()

student3.display_info()
student3.introduce()