import csv
import re
def names_addresses(filename):
    with open(filename) as file:
        next(file)
        for line in file:
            fields = line.strip().split(',') # dirty data problem using split
            name = fields[0]
            address = fields[1]
            print("name =", name, " address =", address)

def names_addresses_csv(filename):
    with open(filename) as file:
        csv_file = csv.reader(file)
        next(csv_file)
        for record in csv_file: # each record is a sequence of fields, already splitted
            name = record[0]
            address = record[1]
            print("Aame =", name, " Address =", address)
def average(filename, column):
    with open(filename) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        sum = 0
        students = 0
        for record in csv_reader:
            score = float(record[column])
            students += 1
            sum += score
        print("Average =", sum/students)

def zip_check(filename):
    with open(filename) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for record in csv_reader:
            address = record[1]
            if re.findall('[789]\d{4}', address):
                print(record[0])
def main():
    # names_addresses("data/full_grades_010.csv")
    # names_addresses_csv("data/full_grades_010.csv")
    # average("data/full_grades_010.csv", 4)
    # if re.findall('a', 'xyzabca'): # -non empty is consider as true
    #     print("Non Empty")
    # else:
    #     print("Empty")
    zip_check("data/full_grades_010.csv")

main()