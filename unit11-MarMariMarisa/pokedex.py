import csv
import pokemon
import random
class Pokedex:
    __slots__ = ["__pokelist"]
    def __init__(self):
        self.__pokelist = []

    def load(self,filename):
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for record in csv_reader:
                self.__pokelist.append(pokemon.Pokemon(record[0],record[1].lower(),int(record[2]),int(record[3])))
        return self.__pokelist
    
    def create_parties(self):
        party_1 = set()
        party_2 = set()
        temp_list = self.__pokelist
        random.shuffle(temp_list)
        for value in range(0,6):
            random_1 = random.randint(0,len(temp_list)-1)
            party_1.add(temp_list[random_1])
            temp_list.pop(random_1)
            random_2 = random.randint(0,len(temp_list)-1)
            party_2.add(temp_list[random_2])
            temp_list.pop(random_2)
        return party_1,party_2
