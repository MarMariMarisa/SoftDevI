import re
def make_letter_frequency(filename):
    dictionary = dict()
    with open(filename) as file:
        for line in file:
            line.lower()
            for ch in line:
                letters = re.findall("[a-z]", ch)
                for chr in letters:
                    if chr in dictionary:
                        dictionary[chr] += 1
                    else:
                        dictionary[chr] = 1
    return dictionary

def print_letter_frequency(dictionary):
    max_num = 0 
    elt_of_max = None
    for elt in dictionary:
        if dictionary[elt] > max_num:
            max_num = dictionary[elt]
            elt_of_max = elt
        print(elt,":",dictionary[elt])
    print("the most populat letters is:",elt_of_max,":",dictionary[elt_of_max])
   

def main():
    dictionary = make_letter_frequency("data/alice.txt")
    print_letter_frequency(dictionary)

if __name__ == "__main__":
    main()
