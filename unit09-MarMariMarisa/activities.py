from itertools import count
import arrays
import time
import random
import math
import re
import arrays
def unique_array(an_array,value):
    for i in range(len(an_array)):
        if an_array[i] == value:
            return
        if an_array[i] == None:
            an_array[i] = value

def fill_array(length):
    an_array = arrays.Array(length)
    start = time.perf_counter()
    for i in range(length):
        unique_array(an_array,i)
    end = time.perf_counter()
    return end -start

def unique_list(a_list,value):
    for elt in a_list:
        if elt == value:
            return
    a_list.append(value)

def fill_list(length):
    a_list = []
    start = time.perf_counter()
    for i in range(length):
        unique_list(a_list,i)
    end = time.perf_counter()
    return end -start
def unique_set(a_set,value):
    a_set.add(value)
def fill_set(length):
    a_set = set()
    start = time.perf_counter()
    for i in range(length):
        unique_list(a_set,i)
    end = time.perf_counter()
    return end -start
def sets():
    x = {10,20,30,40}
    print(x)
    x.add(50)
    x.add(60)
    print(x)
def coupon_collection(n):
    boxes = 0
    collection = set()
    while len(collection) < n:
        coupon = random.randint(1,n)
        collection.add(coupon)
        boxes += 1
    return boxes
def mixup():
    a_set = set("abcdefaaabbb")
    for elt in a_set:
        print(elt,end= " ")
    print()

def count_words(filename):
    counter = {}
    with open(filename) as file:
        for line in file:
            words = line.lower().split()
            for word in words:
                matches = re.findall("[\w]+", word)
                for match in matches:
                    if match in counter:
                        counter[match] = counter[word]+1
                    else:
                        counter[match] = 1
    return counter

def count_words_challenge(filename):
    counter = {}
    with open(filename) as file:
        for line in file:
            words = line.lower().split()
            for word in words:
                matches = re.findall("[\w]+", word)
                for match in matches:
                    if match in counter:
                        counter[match] = counter[word]+1
                    else:
                        counter[match] = 1
    max_value = -1
    max_key = None
    for key in counter:
        value = counter[key]
        if max_value < value:
            max_value = value
            max_key = key

    values = counter.values()
    sorted_values = sorted(values,reverse = True)
    return counter,max_key,max_value

def unique_words(filename): #alice rabbit Alice bye rabbit ## 3 words
    unique_collection = set()
    with open(filename) as file:
        for line in file:
            line = line.lower()
            words = line.split() #["alice","rabbit","Alice","Bye"]
            for word in words:
                matches = re.findall("[\w]+", word)
                for match in matches:
                    unique_collection.add(word)

                
    return unique_collection

def union(a_set,b_set):
    c_set = set()
    for elt in a_set:
        c_set.add(elt)
    for elt in b_set:
        c_set.add(elt)
 
def intersection(a_set,b_set):
    c_set = set()
    for elt in a_set:
        if elt in b_set:
            c_set.add(elt)

def hashes():
    hashcode1 = hash("Hello World!")
    hashcode2 = hash("Hello world!")
    print(hashcode1)
    print(hashcode2)
    hashcode3 = hash("A" * 100000)
    print(hashcode3)
    hashcode4 = hash("A" * 10000000000)
    print(hashcode4)

def collisions(filename,length,hash_func = hash):
    table = arrays.Array(length)
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            hashcode = hash_func(line)
            index = hashcode % length
            if table[index] == None:
                table[index] = line
            else:
                return count
        return count
def ascii_codes(a_string):
    for ch in a_string:
        print(ch,":",ord(ch))
def string_hash(a_string):
    max_ascii = -1
    for ch in a_string:
        ascii = ord(ch)
        if max_ascii < ascii:
            max_ascii = ascii
    return max_ascii
def main():
    # hash1 = string_hash("abcde")
    # hash2 = string_hash("ABCeD")
    count = collisions('data/alice.txt',100,hash)
    print(count)
    count = collisions('data/alice.txt',100,string_hash)
    print(count)
    # hashes()
    # hashes()
    # counter,max_key,max_value = count_words_challenge('data/alice.txt')#,{'alice,',:10,'alice!',:12,'alice,',:10,}
    # # print(counter['rabbit'])
    # # print(counter['alice'])
    # # if "bob" in counter():
    # #     print(counter['bob'])

    # print(max_key,":",max_value)

    # a_set = {10,20,30}
    # b_set = {20,50,30,40}
    # c_set = intersection(a_set,b_set)
    # print(c_set)
    # a_set = unique_words("data/alice.txt")
    # print(a_set)
    # print(len(a_set))
    # mixup()
    # mixup()
    # mixup()
    # elapsed_time = fill_set(5000)
    # # print(elapsed_time)
    # n = 10000
    # boxes = coupon_collection(n)
    # print(boxes)
    # print(n*math.log(n) + 0.57721566*n)
if __name__ == "__main__":
    main()