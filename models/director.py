from .student import Student
from .teacher import Teacher
from .course import Course

class Director:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.courses = []

    def set_director(self, first_name, last_name, age, address):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_course(self, course):
        self.courses.append(course)

    def assign_course(self, teacher, course):
        teacher.add_course(course)

    def get_students(self, level=None):
        return [student for student in self.students if level is None or student.level == level]

    def get_teachers(self):
        return self.teachers

    def get_courses(self):
        return self.courses

    def get_students_with_teacher_for_course(self):
        result = {}
        for course in self.courses:
            teacher = next((teacher for teacher in self.teachers if course in teacher.courses), None)
            result[course.name] = {
                'teacher': str(teacher) if teacher else "None",
                'students': [str(student) for student in course.students]
            }
        return result
