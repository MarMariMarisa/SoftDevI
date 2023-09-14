"""
A Student class.

@author GCCIS Faculty
"""

GRADES = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F", "NG"]

QUALITY_POINTS = {
    GRADES[0]: 4.0,
    GRADES[1]: 3.67,
    GRADES[2]: 3.33,
    GRADES[3]: 3.0,
    GRADES[4]: 2.67,
    GRADES[5]: 2.33,
    GRADES[6]: 2.0,
    GRADES[7]: 1.67,
    GRADES[8]: 1.0,
    GRADES[9]: 0,
    GRADES[10]: 0 # no grade
}

class Student:
    """
    A class that represents a student with fields for ID, name, credits, and
    GPA.
    """
    __slots__ = ["__id", "__name", "__credits", "__gpa","__courses"]

    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__credits = 0
        self.__gpa = 0
        self.__courses = []
    def add_course(self,a_course):
        self.__courses.append(a_course)
        self.__credits += a_course.get_credits()
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_credits(self):
        return self.__credits
    def get_gpa(self):
        if self.__credits == 0:
            return 0
        total_points = 0
        for course in self.__courses:
            total_points += course.get_points()
        return total_points / self.__credits

    def set_gpa(self,gpa):
        self.__gpa = gpa
    def print_student(self):
        print("Student: ID=", self.get_id(), ", name=", self.get_name(), 
            ", credits=", self.get_credits(), ", GPA=", self.get_gpa(), sep="")
class Course:
    __slots__ = ["__name","__credits","__grade"]# "GCIS-123",4,"A-"

    def __init__(self,name,credits):
        self.__name = name
        self.__credits = credits
        self.__grade = "F"
    def get_points(self):
        return QUALITY_POINTS[self.__grade] * self.__credits
    def get_name(self):
        return self.__name
    def get_credits(self):
        return self.__credits
    def get_grade(self):
        return self.__grade
    
    def set_grade(self,grade):
        self.__grade = grade










def print_student(student):
    """
    Prints a student's info to standard output.
    """
    print("Student: ID=", student.get_id(), ", name=", student.get_name(), 
        ", credits=", student.get_credits(), ", GPA=", student.get_gpa(), sep="")