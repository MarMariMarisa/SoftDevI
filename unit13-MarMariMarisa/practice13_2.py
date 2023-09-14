import csv
import node_stack
import random
NAMES_LIST = ["Mary","Sue","Joe","Harry","Marisa","Nathan","Ell","Indigo","Samara","Olivia","Garrett","Remi","Rownan","Kenneth","Gill","Rain","Mars","Ethan","Madi","Grayson","Parker","Ian","Kyle","Destini","Taylor","Hannah","John","Javier","Alex","Clarke","Alejandro","Bella","Angel","Selena","Nancy","Brooke","Tiffany","Peyton","Mikey",
'Krista']
class Exam:
    __slots__ = ["__student_name","__pos_points","__points_earned"]
    def __init__(self,student_name,pos_points):
        self.__student_name = student_name
        self.__pos_points= pos_points
        self.__points_earned = 0
    
    def get_name(self):
        return self.__student_name
    def get_pos_points(self):
        return self.__pos_points
    def get_earned(self):
        return self.__points_earned

    def earn_points(self,earned):
        self.__points_earned += earned
    def lost_points(self,lost):
        self.__points_earned -= lost
    def set_total_score(self,score):
        self.__points_earned = score

    def get_grade(self):
        return (self.__points_earned / self.__pos_points) * 100

    def __str__(self):
        return self.__student_name + ": (" + str(self.get_grade()) + ")"
    def __eq__(self,other):
        return self.__student_name == other.__student_name
    def __lt__(self,other):
        return other.__points_earned > self.__points_earned
    def __gt__(self,other):
        return other.__points_earned < self.__points_earned
    def __hash__(self):
        return hash(self.__student_name)

    def sort(self,other):
        #im not sure how to go about the sorting 
        pass
#functions for the street problems
def read_streets(filename):
    with open(filename) as csv_file:
        street_list = []
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for record in csv_reader:
            name = record[0]
            type = record[1]
            street_list.append((name,type))
    return street_list

def count_types(street_list,type):
    type_count = 0
    for elt in street_list:
        if elt[1].lower() == type.lower():
            type_count += 1
    return type_count

def check_exist(street_list,street,type):
    for elt in street_list:
        if elt[0].lower() == street.lower() and elt[1].lower() == type.lower():
            return True
    return False

def make_type_list_for_street(street_list,name):
    list = []
    for elt in street_list:
        if elt[0].lower() == name.lower():
            list.append(elt[1])
    return list
#end of functions for the street problems
#functions for the exam problems
def collect_exams(exam,stack):
    stack.push(exam)
    return stack
def grade_exams(stack):
    graded_stack = node_stack.Stack()
    while stack.is_empty() == False:
        print("hello?")
        exam = stack.pop()
        exam.earn_points(random.randint(50,100))
        graded_stack.push(exam)
    return graded_stack
def enter_exams(graded_stack):
    exam_data = node_stack.Stack()
    print(graded_stack.is_empty())
    #this is where my code breaks im not sure why graded stack is empty
    while graded_stack.is_empty() == False:
        exam = graded_stack.pop(0)
        exam_data.push(exam)  
    return exam_data

#end of functions for the exam priblems

def main():
    #street problems
    street_list = read_streets("data/streets.csv")
    drive_count = count_types(street_list,"DR")
    print("There are",drive_count,"number of drives\n")

    red_leaf_exist = check_exist(street_list,"RED LEAF","LN")
    print("Red leaf ln exists =",red_leaf_exist,"\n")

    type_list = make_type_list_for_street(street_list,"VISTA")
    print("List of street types")
    for type in type_list:
        print("\t",type)
    print("")
    #end of street problems
    #exam problems
    ungraded_exam_stack = node_stack.Stack()
    print("Administering Exams")
    for _ in range(0,30):
        random.shuffle(NAMES_LIST)
        exam = Exam(NAMES_LIST.pop(),100)
        print("\tCompleted:",str(exam))
        ungraded_exam_stack = collect_exams(exam,ungraded_exam_stack)
    
    print("Grading Exams")
    graded_stack = grade_exams(ungraded_exam_stack)
    holder = graded_stack
    while holder.is_empty() == False:
        print("\tGraded:",str(holder.pop()))

    print("Entering grades into grade database:")
    exam_data = enter_exams(graded_stack)
    holder = exam_data
    while holder.is_empty() == False:
        print("bruh")
        print("\tEntered:",str(holder.pop()))

    
    #end of exam problems


main()