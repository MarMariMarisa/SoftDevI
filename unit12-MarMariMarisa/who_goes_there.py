import csv
import list_stack
import random

class Task:
    __slots__ = ["__name", "__location"]
    def __init__(self, name, location):
        self.__name = name
        self.__location = location
    def get_location(self):
        return self.__location
    def __str__(self):
        return self.__name + " in " + self.__location
class Crewmate:
    __slots__ = ["__color","__task_collection","__murdered"]
    def __init__(self,color):
        self.__color = color
        self.__task_collection = list_stack.Stack()
        self.__murdered = False
    def assign_task(self,task):
       self.__task_collection.push(task)
    def set_murder(self):
        self.__murdered = True
    def get_color(self):
        return self.__color
    def get_murdered(self):
        return self.__murdered
    def get_tasks(self):
        return self.__task_collection.get_stack()
    def __str__(self):
        return "Crewmate:\n" + "\tColor= " + str(self.__color) + "\n\tMurdered = " + str(self.__murdered) + "\n\tTasks: " + str(self.__task_collection)
    def __repr__(self,crewmate):
        ring = "Crewmate:\n" + "\tColor= " + str(self.__color)
        if crewmate.get_murdered() == True:
            return str(ring) + " (deceased)"
        else:
            return ring
class Ship:
    __slots__ = ["__locations","__tasks","__imposter_num","__crew","__location_list"]
    def __init__(self, tasks,num_imposters):
        CREWMATE_COLORS = ["Black","Blue","Brown","Cyan","Green","Pink","Purple","Red","White","Yellow"]
        self.__tasks = tasks
        self.__locations = dict()
        self.__crew = list_stack.Stack()
        self.__location_list = []
        for key in self.__tasks:
            self.__location_list.append(key)
            self.__locations[key] = False # true or falsse if imposter is present
        if num_imposters > 4 or num_imposters < 1:
            raise ValueError("Invalid Number of impostes")
        else:
            self.__imposter_num = num_imposters
        for _ in range(0,10-self.__imposter_num):
            #print(CREWMATE_COLORS)
            num = random.randint(0,len(CREWMATE_COLORS)-1)
            color = CREWMATE_COLORS.pop(num)
            crewmate = Crewmate(color)
            self.__crew.push(crewmate)
        for crewmate in self.__crew.get_stack():
            for _ in range(0,random.randint(3,6)):
                location = self.__location_list[random.randint(0,len(self.__location_list)-1)]
                pos_tasks = self.__tasks[location]
                task = pos_tasks[random.randint(0,len(pos_tasks)-1)]
                crewmate.assign_task(Task(task,location))
    def get_crew(self):
        return self.__crew
    def get_imposter_num(self):
        return self.__imposter_num
    def complete_tasks(self):
        cafeteria  = []
        for crewmate in self.__crew.get_stack():
            if crewmate.get_murdered() == False:
                cafeteria.append(crewmate)
        for _ in range(0,self.__imposter_num-1):
             location = self.__location_list[random.randint(0,len(self.__location_list)-1)]
             self.__locations[location] = True
        for crewmate in cafeteria:
            if len(crewmate.get_tasks()) > 0:
                task = crewmate.get_tasks().pop()
                print(str(crewmate.get_color()) + " begins to " + str(task))
                if self.__locations[task.get_location()] == True:
                    print("\tOh no! An imposter was waiting in ambush!", crewmate.get_color()," Crewmate is murdered!")
                    crewmate.set_murder()
                else:
                    print("\tTask is complete!")
                    if len(crewmate.get_tasks()) > 0:
                        print(crewmate.get_color()," Crewmate heads back to the cafeteria")
                    else:
                        print(crewmate.get_color(),"Crewmate has finished all there tasks!")
        for crewmate in self.__crew.get_stack():
            if crewmate.get_murdered() == False:
                if len(crewmate.get_tasks()) > 0:
                    self.complete_tasks() 
                 
def get_tasks(filename):
    tasks = dict()
    with open(filename) as file:
            csv_file = csv.reader(file)
            next(csv_file)
            for line in csv_file:
                location = line[1]
                task = line[0]
                if not location in tasks:
                    tasks[location] = [task]
                else:
                    tasks[location].append(task)
    return tasks

def main():
    tasks = get_tasks("tasks_01.csv")
    ship = Ship(tasks,3)
    ship.complete_tasks()
    print("The journey has ended!")
    survived = False
    for crewmate in ship.get_crew().get_stack():
        if crewmate.get_murdered() == False:
            survived = True
    if survived == True:
        print("The crew made it!")
        for crewmate in ship.get_crew().get_stack():
            ring = str(crewmate.get_color()) + " Crewmate "
            if crewmate.get_murdered() == True:
                ring = ring + "(Deceased)"
            print(ring)
    else:
        print("The imposter won.")
                            #for crewmate in self.__crew.get_stack():

main()