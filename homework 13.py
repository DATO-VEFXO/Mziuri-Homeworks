class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def get_info(self):
        return f"{self.first_name} {self.last_name}"
class School:
    def __init__(self, school_name, address):
        self.school_name = school_name
        self.address = address
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    def remove_student(self, index):
        if 0 <= index < len(self.students):
            del self.students[index]
        else:
            print("indeqsi arasworia")
    def show_students(self):
        for student in self.students:
            print(student.get_info())
school1 = School("sajaro skola n60", "Tbilisi")
student1 = Student("dato","vefxvadze")
student2 = Student("ana", "chantladze")
student3 = Student("zuka", "beridze")
student4 = Student("bela", "prozorova")
school1.add_student(student1)
school1.add_student(student2)
school1.add_student(student3)
school1.add_student(student4)
school1.show_students()