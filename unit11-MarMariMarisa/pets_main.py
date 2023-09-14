import pets
def main():
    dog = pets.Pet("dog","Happy",50,"brown",10)
    cat = pets.Pet("Regular","Meow",1,"black",2)
    print("Name:",dog.get_name,"Weight:",dog.get_weight)
    # print("Name:",cat.name,"Weight:",cat.weight)
    # dog.feed(1800)
    # # print("Name:",dog.name,"Weight:",dog.weight)
    # # dog.walk(1.5)
    # # print("Name:",dog.name,"Weight:",dog.weight)
    # dog.__weight += 100



main()