import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from models.student import Student
from models.teacher import Teacher
from models.course import Course
from models.director import Director


# Create an instance of the Director class
director = Director()
director.set_director("John", "Doe", 50, "123 Main St")

# Create the GUI
root = tk.Tk()
root.title("Education Management System")

# Tabs for the GUI
tab_control = ttk.Notebook(root)

student_tab = ttk.Frame(tab_control)
teacher_tab = ttk.Frame(tab_control)
director_tab = ttk.Frame(tab_control)

tab_control.add(student_tab, text='Student')
tab_control.add(teacher_tab, text='Teacher')
tab_control.add(director_tab, text='Director')
tab_control.pack(expand=1, fill='both')

# GUI for Students
def student_search_courses():
    date = simpledialog.askstring("Input", "Enter date (YYYY-MM-DD):")
    if date:
        student_name = simpledialog.askstring("Input", "Enter your full name:")
        for student in director.get_students():
            if student.first_name + " " + student.last_name == student_name:
                courses = student.get_courses_on_date(date, director.get_courses())
                course_names = [course.name for course in courses]
                messagebox.showinfo("Courses on " + date, "\n".join(course_names))
                return
        messagebox.showerror("Error", "Student not found.")

tk.Button(student_tab, text="Search Courses", command=student_search_courses).pack()

# GUI for Teachers
def teacher_search_courses():
    date = simpledialog.askstring("Input", "Enter date (YYYY-MM-DD):")
    if date:
        teacher_name = simpledialog.askstring("Input", "Enter your full name:")
        for teacher in director.get_teachers():
            if teacher.first_name + " " + teacher.last_name == teacher_name:
                courses = teacher.get_courses_on_date(date)
                course_names = [course.name for course in courses]
                messagebox.showinfo("Courses on " + date, "\n".join(course_names))
                return
        messagebox.showerror("Error", "Teacher not found.")

tk.Button(teacher_tab, text="Search Courses", command=teacher_search_courses).pack()

def teacher_view_students_and_courses():
    teacher_name = simpledialog.askstring("Input", "Enter your full name:")
    for teacher in director.get_teachers():
        if teacher.first_name + " " + teacher.last_name == teacher_name:
            info = ""
            for course in teacher.courses:
                student_names = [student.first_name + " " + student.last_name for student in course.students]
                info += f"Course: {course.name}\nStudents: {', '.join(student_names)}\n\n"
            messagebox.showinfo("Courses and Students", info)
            return
    messagebox.showerror("Error", "Teacher not found.")

tk.Button(teacher_tab, text="View Students and Courses", command=teacher_view_students_and_courses).pack()

def assign_grades():
    grade_window = tk.Toplevel(root)
    grade_window.title("Assign Grades")

    tk.Label(grade_window, text="Select Course:").pack()
    course_combobox = ttk.Combobox(grade_window, values=[course.name for course in director.get_courses()])
    course_combobox.pack()

    tk.Label(grade_window, text="Select Teacher:").pack()
    teacher_combobox = ttk.Combobox(grade_window, values=[teacher.first_name + " " + teacher.last_name for teacher in director.get_teachers()])
    teacher_combobox.pack()

    tk.Label(grade_window, text="Select Student:").pack()
    student_combobox = ttk.Combobox(grade_window, values=[f"{student.first_name} {student.last_name}" for student in director.get_students()])
    student_combobox.pack()

    tk.Label(grade_window, text="Enter Grade:").pack()
    grade_entry = tk.Entry(grade_window)
    grade_entry.pack()

    tk.Button(grade_window, text="Assign Grade", command=lambda: assign_selected_grade(course_combobox, teacher_combobox, student_combobox, grade_entry)).pack()

def assign_selected_grade(course_combobox, teacher_combobox, student_combobox, grade_entry):
    course_name = course_combobox.get()
    teacher_name = teacher_combobox.get()
    student_name = student_combobox.get()
    grade = grade_entry.get()

    try:
        grade = float(grade)
    except ValueError:
        messagebox.showerror("Error", "Invalid grade value.")
        return

    course = next((c for c in director.get_courses() if c.name == course_name), None)
    teacher = next((t for t in director.get_teachers() if t.first_name + " " + t.last_name == teacher_name), None)
    student = next((s for s in director.get_students() if s.first_name + " " + s.last_name == student_name), None)

    if course and teacher and student:
        try:
            teacher.assign_grade(course, student, grade)
            messagebox.showinfo("Success", "Grade assigned successfully.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showerror("Error", "Course, Teacher, or Student not found.")

def teacher_view_grades():
    course_name = simpledialog.askstring("Input", "Enter course name:")
    course = next((c for c in director.get_courses() if c.name == course_name), None)
    if course:
        grades = course.get_grades()
        info = "\n".join([f"{student}: {grade}" for student, grade in grades.items()])
        messagebox.showinfo("Grades", info)
    else:
        messagebox.showerror("Error", "Course not found.")

tk.Button(teacher_tab, text="View Grades", command=teacher_view_grades).pack()

# GUI for Director
def add_student():
    first_name = simpledialog.askstring("Input", "Enter first name:")
    last_name = simpledialog.askstring("Input", "Enter last name:")
    age = simpledialog.askinteger("Input", "Enter age:")
    address = simpledialog.askstring("Input", "Enter address:")
    level = simpledialog.askstring("Input", "Enter level (Level 1, Level 2, Level 3):")
    student = Student()
    student.set_student(first_name, last_name, age, address, level)
    try:
        director.add_student(student)
        messagebox.showinfo("Success", "Student added successfully.")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def add_teacher():
    first_name = simpledialog.askstring("Input", "Enter first name:")
    last_name = simpledialog.askstring("Input", "Enter last name:")
    age = simpledialog.askinteger("Input", "Enter age:")
    address = simpledialog.askstring("Input", "Enter address:")
    teacher = Teacher()
    teacher.set_teacher(first_name, last_name, age, address)
    try:
        director.add_teacher(teacher)
        messagebox.showinfo("Success", "Teacher added successfully.")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def add_course():
    name = simpledialog.askstring("Input", "Enter course name:")
    start_date = simpledialog.askstring("Input", "Enter start date:")
    end_date = simpledialog.askstring("Input", "Enter end date:")
    course = Course()
    course.set_course(name, start_date, end_date)
    try:
        director.add_course(course)
        messagebox.showinfo("Success", "Course added successfully.")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def show_courses():
    courses_info = director.get_students_with_teacher_for_course()
    info = ""
    for course, details in courses_info.items():
        info += f"Course: {course}\nTeacher: {details['teacher']}\nStudents: {', '.join(details['students'])}\n\n"
    messagebox.showinfo("Courses Information", info)

def assign_teacher_and_students():
    assign_window = tk.Toplevel(root)
    assign_window.title("Assign Teacher and Students to Course")

    tk.Label(assign_window, text="Select Course:").pack()
    course_combobox = ttk.Combobox(assign_window, values=[course.name for course in director.get_courses()])
    course_combobox.pack()

    tk.Label(assign_window, text="Select Teacher:").pack()
    teacher_combobox = ttk.Combobox(assign_window, values=[teacher.first_name + " " + teacher.last_name for teacher in director.get_teachers()])
    teacher_combobox.pack()

    tk.Label(assign_window, text="Select Students (Level 1):").pack()
    students_listbox_level1 = tk.Listbox(assign_window, selectmode=tk.MULTIPLE)
    for student in director.get_students(level="Level 1"):
        students_listbox_level1.insert(tk.END, student.first_name + " " + student.last_name)
    students_listbox_level1.pack()

    tk.Label(assign_window, text="Select Students (Level 2):").pack()
    students_listbox_level2 = tk.Listbox(assign_window, selectmode=tk.MULTIPLE)
    for student in director.get_students(level="Level 2"):
        students_listbox_level2.insert(tk.END, student.first_name + " " + student.last_name)
    students_listbox_level2.pack()

    tk.Label(assign_window, text="Select Students (Level 3):").pack()
    students_listbox_level3 = tk.Listbox(assign_window, selectmode=tk.MULTIPLE)
    for student in director.get_students(level="Level 3"):
        students_listbox_level3.insert(tk.END, student.first_name + " " + student.last_name)
    students_listbox_level3.pack()

    tk.Button(assign_window, text="Assign", command=lambda: assign_selected_teacher_and_students(course_combobox, teacher_combobox, students_listbox_level1, students_listbox_level2, students_listbox_level3)).pack()

def assign_selected_teacher_and_students(course_combobox, teacher_combobox, students_listbox_level1, students_listbox_level2, students_listbox_level3):
    course_name = course_combobox.get()
    teacher_name = teacher_combobox.get()
    selected_students = students_listbox_level1.curselection() + students_listbox_level2.curselection() + students_listbox_level3.curselection()

    course = next((c for c in director.get_courses() if c.name == course_name), None)
    teacher = next((t for t in director.get_teachers() if t.first_name + " " + t.last_name == teacher_name), None)

    if course and teacher:
        for i in selected_students:
            student_name = students_listbox_level1.get(i) or students_listbox_level2.get(i) or students_listbox_level3.get(i)
            student = next((s for s in director.get_students() if s.first_name + " " + s.last_name == student_name), None)
            if student:
                course.add_student(student)
        teacher.add_course(course)
        messagebox.showinfo("Success", "Teacher and students assigned to course successfully.")
    else:
        messagebox.showerror("Error", "Course or Teacher not found.")

tk.Button(director_tab, text="Add Student", command=add_student).pack()
tk.Button(director_tab, text="Add Teacher", command=add_teacher).pack()
tk.Button(director_tab, text="Add Course", command=add_course).pack()
tk.Button(director_tab, text="Show Courses", command=show_courses).pack()
tk.Button(director_tab, text="Assign Teacher and Students", command=assign_teacher_and_students).pack()

root.mainloop()

