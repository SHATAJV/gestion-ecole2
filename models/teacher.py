from .person import Person

class Teacher(Person):
    def __init__(self):
        self.courses = []

    def set_teacher(self, first_name, last_name, age, address):
        self.set_person(first_name, last_name, age, address)

    def add_course(self, course):
        self.courses.append(course)

    def assign_grade(self, course, student, grade):
        if course in self.courses and student in course.students:
            course.assign_grade(student, grade)
        else:
            raise ValueError("Course or student not found")

    def get_courses_on_date(self, date):
        return [course for course in self.courses if date in course.get_dates()]
