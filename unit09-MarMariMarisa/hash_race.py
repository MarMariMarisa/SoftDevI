from turtle import pos, position
import time

def hash_first_char(a_string):
    if a_string == None or len(a_string) == 0:
        return 0
    else:
        char = a_string[0]
        return ord(char)
    
def hash_sum(a_string):
    if a_string == None or len(a_string) == 0:
        return 0
    else:
        sum = 0
        for char in a_string:
            sum += ord(char)
        return sum

def hash_positional_sum(a_string):
    if a_string == None or len(a_string) == 0:
        return 0
    else:
        positional_sum = 0
        for i in range(len(a_string)):
            positional_sum = positional_sum + (ord(a_string[i]) * 31 ** (len(a_string) - (i+1)))
        return positional_sum

def build_collision_counter(hash_func,filename):
    dictionary = dict()
    #open file
    with open(filename) as file:
        for line in file:
            hashcode = hash_func(line)
            if hashcode in dictionary:
                dictionary[hashcode] = dictionary[hashcode] + 1
            else:
                 dictionary[hashcode] = 0
    return dictionary
def get_collision_rate(dictionary):
    number_of_collisions = 0
    for key in dictionary:
        if dictionary[key] != 0:
            number_of_collisions += 1
    if number_of_collisions != 0:
        number_of_collisions -= 1
    collision_rate = number_of_collisions / len(dictionary)
    return collision_rate
def get_max_number(dictionary):
    max_number = 0
    for key in dictionary:
        if dictionary[key] > max_number:
            max_number = dictionary[key]
    return max_number
def get_spread(dictionary):
    with open("data/long_line_words.txt") as file:
        nol = 0
        for line in file:
            nol +=1
    return len(dictionary)/ nol
def get_speed(hash_func,filename):
    start = time.perf_counter()
    with open(filename) as file:
        for line in file:
            hash_func(line)
    end = time.perf_counter()
    return end - start
def hash_test(dictionary,hash_func):
    collision_rate = get_collision_rate(dictionary) * 100
    max_number = get_max_number(dictionary)
    spread = get_spread(dictionary) * 100
    speed = get_speed(hash_func,"data/long_line_words.txt")
    print("hash function:",hash_func.__name__)
    print("total collision rate: ", round(collision_rate,2),"%",sep = "")
    print("maximum collisions:",max_number)
    print("spread: ",round(spread,2),"%",sep = "")
    print("speed:",round(speed,2),"seconds")


    
def main():
    hash_func = hash
    dictionary = build_collision_counter(hash_func,"data/long_line_words.txt")
    hash_test(dictionary,hash_func)
    print("")

    hash_func = hash_first_char
    dictionary = build_collision_counter(hash_func,"data/long_line_words.txt")
    hash_test(dictionary,hash_func)
    print("")

    hash_func = hash_sum
    dictionary = build_collision_counter(hash_func,"data/long_line_words.txt")
    hash_test(dictionary,hash_func)
    print("")

    hash_func = hash_positional_sum
    dictionary = build_collision_counter(hash_func,"data/long_line_words.txt")
    hash_test(dictionary,hash_func)

if __name__ == "__main__":
    main()