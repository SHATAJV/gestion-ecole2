from .student import Student
from .teacher import Teacher
from .course import Course


class Director:
    def __init__(self):
        """Initialize the Director with empty lists for students, teachers, and courses."""
        self.students = []
        self.teachers = []
        self.courses = []

    def set_director(self, first_name, last_name, age, address):
        """
        Set the director's personal details.

        Args:
            first_name (str): The first name of the director.
            last_name (str): The last name of the director.
            age (int): The age of the director.
            address (str): The address of the director.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address

    def add_student(self, student):
        """
        Add a student to the director's list of students.

        Args:
            student (Student): The student to add.
        """
        self.students.append(student)

    def add_teacher(self, teacher):
        """
        Add a teacher to the director's list of teachers.

        Args:
            teacher (Teacher): The teacher to add.
        """
        self.teachers.append(teacher)

    def add_course(self, course):
        """
        Add a course to the director's list of courses.

        Args:
            course (Course): The course to add.
        """
        self.courses.append(course)

    def assign_course(self, teacher, course):
        """
        Assign a course to a teacher.

        Args:
            teacher (Teacher): The teacher to assign the course to.
            course (Course): The course to assign.
        """
        teacher.add_course(course)

    def get_students(self, level=None):
        """
        Get a list of students, optionally filtered by level.

        Args:
            level (str, optional): The level to filter students by. Defaults to None.

        Returns:
            list: The list of students.
        """
        return [student for student in self.students if level is None or student.level == level]

    def get_teachers(self):
        """
        Get a list of all teachers.

        Returns:
            list: The list of teachers.
        """
        return self.teachers

    def get_courses(self):
        """
        Get a list of all courses.

        Returns:
            list: The list of courses.
        """
        return self.courses

    def get_students_with_teacher_for_course(self):
        """
        Get a dictionary of courses with the associated teacher and students.

        Returns:
            dict: A dictionary with course names as keys and a dictionary with 'teacher' and 'students' as values.
        """
        result = {}
        for course in self.courses:
            teacher = next((teacher for teacher in self.teachers if course in teacher.courses), None)
            result[course.name] = {
                'teacher': str(teacher) if teacher else "None",
                'students': [str(student) for student in course.students]
            }
        return result
