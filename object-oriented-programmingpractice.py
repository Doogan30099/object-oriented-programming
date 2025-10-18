
class Student: 
    def __init__(self, name, email, grades):
        self.name = name
        self.email = email
        self.grades = grades

    def grades_tuple(self):
        return tuple(self.grades)

    def add_grade(self, grade):
        self.grades.append(grade)
        return f"Added grade {grade} for {self.name}."
    




    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    

    def display_info(self):
        return f"Student Name: {self.name}, Email: {self.email}, Average Grade: {self.average_grade()}"
    
student1 = Student("PJ Nunes", "pjnunes@email.com", [85, 90, 95,80, 100])
student2 = Student("Alexa Nunes", "Alexanunes@email.com", [88, 92, 80, 85, 91])
student3 = Student ("John Doe", "johndoe@email.com", [70, 75, 80, 65, 90])


students_list = [student1, student2, student3]



student_dict = {student.email: student for student in students_list}


def get_student_by_email(email):
    return student_dict.get(email, "Student not found")

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

for student in students_list:
    print(len(student.grades))




