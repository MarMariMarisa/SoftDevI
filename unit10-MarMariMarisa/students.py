from re import S


class Student:
    id = "No ID"
    name = "Student"
    credits = 0
    gpa = 0.0
def print_student(a_student):
    print("Student", a_student.id,)
def main():
    student1 = Student()
    student2 = Student()
    student1.id = "cb1234"
    student1.name = "Charlie Brown"
    student1.credits = 0
    student1.gpa = 0.0
    student1.credits += 3
    student1.gpa = 2.7

    student2.id = "js9999"
    student2.name = "John Smith"
    student2.credits = 12
    student2.gpa = 3.0
    student2.friend("Alice")

    
    print_student(student1)
    print_student(student2)



main()