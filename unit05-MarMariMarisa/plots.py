from distutils.log import error
from msilib.schema import Error
import plotter
# when called this function returns true or false if the user wants to quit
def terminate():
    ui = input("Are you sure you would like to quit?(y/n): ")
    ui = ui.split()
    if ui[0].lower() == "y":
        return True
    if ui[0].lower() == "n":
        return False
    if ui[0].lower() != "y" and ui[0].lower() != "n":
        print("Invalid Input")
#this function displays and tests the quit message
def quit_message(x):
    if x == "quit":
                if terminate() == True:
                    return True
                else:
                    return False
# recieves paranemets and graphs a students various grades based off of them
def plot_grades(filename,first,last):
    found = False
    try:
        with open(filename) as file:
            for line in file:
                fields = line.strip().split(',')
                if fields[1] == first and fields[0] == last:
                    found = True
                    count = 2
                    plotter.init(first + " " + last, "Grade Item", "Score")
                    while len(fields) > count:  
                        try:
                            plotter.add_data_point(float(fields[count])) 
                        except ValueError:
                            plotter.add_data_point(0)
                        count += 1         
            plotter.plot()
            file.close()
            return found
    except:
        raise FileNotFoundError
#this function passes the grades and inputs to plot_grades abd catches errors
def student_grade(input):
    try:
        if plot_grades(input[1],input[2],input[3]) == True:
            print("Plot finished (window may be hidden")
        if plot_grades(input[1],input[2],input[3]) == False:
            print("Plot Failed (no such student)")
    except FileNotFoundError:
        print("No Such File:", input[1])
    except IndexError:
        print("Usage: stu <filename> <first name> <last name>")
#this funciton displays a help message when called
def help():
    print("stu <filename> <first name> <last name> - plot student grades")
    print("quit - quits")
    print("help - displays this message")
#main function
def main():
    going = True
    while going == True:
        try:
            ui = input(">> ")
            if not ui:
                raise ValueError()
            ui = ui.split(" ")
            if ui[0] == "quit":
               if quit_message(ui[0]) == True:
                going = False
            elif ui[0] == "stu":
                student_grade(ui)
            elif ui[0] == "help":
                help()
            else:
                raise ValueError
        except ValueError:
            print("Enter a command (help for list) or 'quit' to quit.")
    print("Goodbye!")
main()