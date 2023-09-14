
def build_x_to_y(filename):
    dictionary = dict()
    with open(filename) as file:
        for line in file:
            tokens = line.split()
            if tokens[0] in dictionary:
                dictionary[tokens[0]].append(tokens[1])
            else:
                dictionary[tokens[0]] = [tokens[1]]
    return dictionary

def build_y_to_x(x_to_y):
    dictionary = dict()
    for key in x_to_y:
        for value in x_to_y[key]:
            if not value in dictionary:
                a_set = set()
                for key in x_to_y:
                    if value in x_to_y[key]:
                            a_set.add(key)
                dictionary[value] = a_set
    return dictionary



def main():
    dictionary = build_x_to_y("data/points_small.txt")
    print(dictionary)
    # 1. Uncomment to test using points_small.txt
    
    x_to_y = build_x_to_y("data/points_small.txt")
    y_to_x = build_y_to_x(x_to_y)
    print("x_to_y =", x_to_y) # {10: [20, 30], 15: [20, 25, 20]}
    print("y_to_x =", y_to_x) # {20: {10, 15}, 30: {10}, 25: {15}}
    

    # 2. Uncomment to test using points.txt

    x_to_y = build_x_to_y("data/points.txt")
    y_to_x = build_y_to_x(x_to_y)
    print(len(x_to_y))
    print(len(y_to_x))
    print("x_to_y[30] =", x_to_y['30'])   # [34, 52, 53]
    print("x_to_y[320] =", x_to_y['320']) # [26]
    print("y_to_x[19] =", y_to_x['19'])   # {458, 906, 651, 500}
    print("y_to_x[46] =", y_to_x['46'])   # {136, 202, 791, 781, 461, 465, 727, 568, 348, 29, 510, 216}
main()
 
