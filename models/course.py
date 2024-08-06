class Course:
    def __init__(self):
        self.name = None
        self.start_date = None
        self.end_date = None
        self.students = []
        self.grades = {}

    def set_course(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date

    def add_student(self, student):
        self.students.append(student)

    def get_dates(self):
        from datetime import datetime, timedelta
        start = datetime.strptime(self.start_date, "%Y-%m-%d")
        end = datetime.strptime(self.end_date, "%Y-%m-%d")
        return [(start + timedelta(days=i)).strftime("%Y-%m-%d") for i in range((end-start).days + 1)]

    def assign_grade(self, student, grade):
        self.grades[student] = grade

    def get_grades(self):
        return {str(student): grade for student, grade in self.grades.items()}
