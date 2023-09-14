import csv
def find_streets(filename,street_name):
    try:
        with open(filename) as file:
                csv_file = csv.reader(file)
                next(csv_file)
                for line in csv_file:
                        name = line[0]
                        type = line[1]
                        direction = line[2]
                        if name.lower() == street_name.lower():
                            print(street_name,type,direction)
    except:
        raise FileNotFoundError
def compare_street_popularity(top,test):
    return test > top
def find_pop_street(filename):
    top = 0
    top_street = ""
    try:
        with open(filename) as file:
                csv_file = csv.reader(file)
                next(csv_file)
                for line in csv_file:
                    street = line[0]
                    counter = 0
                    csv_file = csv.reader(file)
                    next(csv_file)
                    for line in csv_file:
                        if line[1] == street:
                            counter +=1
                    if compare_street_popularity(top,counter) == True:
                        top_street = street
        return top_street
    except:
        raise FileNotFoundError


        
