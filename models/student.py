from .person import Person

class Student(Person):
    def set_student(self, first_name, last_name, age, address, level):
        self.set_person(first_name, last_name, age, address)
        self.courses = []
        self.level = level

    def add_course(self, course):
        self.courses.append(course)

    def get_courses_on_date(self, date, all_courses):
        return [course for course in all_courses if date in course.get_dates()]
