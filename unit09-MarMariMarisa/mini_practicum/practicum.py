def in_place_reverse(a_list): ## O(c)
    new_list = []
    for i in range(len(a_list)):
        new_list.insert(len(new_list),a_list.pop())
    return new_list

def make_multiplication_table():
    return [[r*c for c in range(1,11)]for r in range(1,11)]

def main():
    # print(in_place_reverse(['3','2','1']))
    table = make_multiplication_table()
    for elt in table:
        print(elt)

if __name__ == "__main__":
    main()


