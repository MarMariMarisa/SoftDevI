import students
def main():
    course1 = students.Course("GCIS-123",4)
    course2 = students.Course("Math-180",2)
    print(course1.get_name(),course1.get_credits(),course1.get_grade)
    print(course2.get_name(),course2.get_credits(),course2.get_grade)

    st1 = students.Student(1234,"John Smith")
    st1.add_course(course1)
    st1.add_course(course2)

    course1.set_grade("A-")
    course1.set_grade("B")


    st1.print_student()
    
    # # st2 = students.Student(5678,"Charlie Brown")

    # students.print_student(st1)
    # st1.print_student()



if __name__ == "__main__":
    main()