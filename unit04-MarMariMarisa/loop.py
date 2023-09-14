
def count_down(number):
    sum = 0
    while number >= 0:
        print(number)
        sum+= number
        number = number - 1
        
    return sum
def count_up(number):
    sum = 0
    count = 0
    while count <= number :
        print(count)
        sum+= count
        count += 1   
    return sum
def printChars(string):
    print(string)
    index = 0
    while index < len(string):
        print(string[index])
        index += 1

def whileInput():
    while True:
        number = int(input(">>"))
        if number  == 0:
            break
        elif number % 2 == 0:
            continue
        sum += number

def escapeSequence():  
    s = "She said\"I don\'t like broccoli.\""
    print(s)
    s = "She \t\t said \"I \\\ndon't \t\t like \\"
    print(s)

def print_range(a_range):
    index = 0
    while index < len(a_range):
        print(a_range[index], end = ' ')
        index+=1
    print()

def print_range_for(a_range):
    for elt in a_range:
        print(elt, end = ' ')
    print()
def reverse(a_string):
    reversed = ''
    for chr in a_string:
        reversed = chr + reversed    
    return reversed
def split_print(a_string, a_delimiter = None):
    tokens = a_string.split(a_delimiter)
    for token in tokens:
        print(token)
def main():
    sum = count_down(50)
    # print("sum:", sum)
    # print("-------------------")
    # sum = count_up(50)
    # print("sum:", sum)
    # printChars("Hello!")
    # whileInput()
    # a_range = range(11)
    # a_range= range(0,21,2)
    # a_range = range(5,17,2)
    # # a_range = range(10,-1,-1)
    # # print_range(a_range)
    # # print_range_for(a_range)
    # print(reverse("Hello World!"))
    a_string = "Abc--de--fgh-bruh--hehe"
    split_print(a_string, "--")
main()