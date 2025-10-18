#  create a student class
class Student: 
    def __init__(self, name, email, grades):
        self.name = name
        self.email = email
        self.grades = grades
# method to return grades as tuple
    def grades_tuple(self):
        return tuple(self.grades)
# add method to add grade
    def add_grade(self, grade):
        self.grades.append(grade)
        return f"Added grade {grade} for {self.name}."
    



# method to calculate average grade
    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
# method to display student info
    def display_info(self):
        return f"Student Name: {self.name}, Email: {self.email}, Average Grade: {self.average_grade()}"
    # create 3 different student objects
student1 = Student("PJ Nunes", "pjnunes@email.com", [85, 90, 95,80, 100])
student2 = Student("Alexa Nunes", "Alexanunes@email.com", [88, 92, 80, 85, 91])
student3 = Student ("John Doe", "johndoe@email.com", [70, 75, 80, 65, 90])

# add grades to each student
Student1.add_grade(87)
Student2.add_grade(89)

# display student information
print(student1.display_info())
print(student2.display_info())
print(student3.display_info())


# create a list of students
students_list = [student1, student2, student3]


# create a dictionary with email as key and student object as value
student_dict = {student.email: student for student in students_list}

# function to get student by email 
def get_student_by_email(email):
    return student_dict.get(email, "Student not found")

# test tuple immutability with try-except error handling
try:
    grade_tuple = student1.grades_tuple()
    grade_tuple[0] = 100 
except TypeError as e:
    print(f"Error: Cannot modify grades tuple - {e}")

# pop last grade from each student
for student in students_list:
    student.grades.pop(-1)



# Print first and last grade from each student
for student in students_list:
    first_grade = student.grades[0]
    last_grade = student.grades[-1]
    print(f"{student.name}: First grade = {first_grade}, Last grade = {last_grade}")
# Print number of grades for each student
for student in students_list:
    print(len(student.grades))




