import students
def main():
    st1 = students.Student(1234,"John Smith")
    st2 = students.Student(5678,"Charlie Brown")

    students.print_student(st1)
    st1.print_student()



if __name__ == "__main__":
    main()