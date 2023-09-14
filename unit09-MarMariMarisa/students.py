def make_students(id,name):
    return  [id,name,0,0.0]
def add_student(population,id,name):
    for index in range(len(population)):
        if population[index][0] == id:
            population.pop(index)
            break
    new_student = make_students(id,name)
    population.append(new_student)

    # population = population + [new_student]
def get_student(population,id):
    for student in population:
        if student[0] == id:
            return student

def add_credits(population,id,credits):
    student = get_student(population,id)
    if student != None:
        student[2] += credits

def get_credit(population,id):
    student = get_student(population,id)
    if student != None:
        return student[2]
    else:
        return None

def names():
    name = {}
    names["J"]
    names["T"]
    names["S"]
    print(names)

    names["J"] = "Jack"
    names["T"] = "Tommy"

    name = names["S"]
    print(names)
    if "K" in names:
        name = names["K"]
        print(name)
        

def main():
    st1 = make_students("cb1234","Charlie Brown")
    st2 = make_students("sb999", "Sally Brown")
    st3 = make_students("js5678","John Smith")
    population = [] ## --> {}
    add_student(population,"cb1234","Charlie Brown" )
    add_student(population,"sb999", "Sally Brown" )
    add_student(population,"js5678","John Smith" )
    add_student(population,"sb999", "Sam B" )
    print(population)
    st = get_student(population,"cb12345")
    add_credits(population,"cb1234",4)
    
    credits = get_credit(population,"cb1234")
    print(credits)

    #print(population)

main()