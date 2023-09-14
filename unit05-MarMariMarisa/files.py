import plotter
def print_lines(filepath):
    file = open(filepath)
    for line in file:
        stripped = line.strip()
        print(len(stripped), stripped)
    file.close()

def word_search(filepath):
    user_word = input("Please enter a word: ")
    user_word.lower()
    file = open(filepath)
    is_found = False
    for line in file:
        word = line.strip()
        if word.lower() == user_word:
            print("Word",user_word, "found")
            is_found = True
            break
    if is_found == False:
        print(user_word, "Not found")
    file.close()
def longest_word(string):
    if string.strip() == "":
        return
    words = string.split()
    longest_word = ''
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    print(longest_word)


def longest_words(filepath):
    file = open(filepath)
    for line in file:
        longest_word(line)
    file.close()

def print_names(filename):
    file = open(filename)
    next(file) # skip the header
    for line in file:
        fields = line.strip().split(',') #['foel','Endre','94]
        first_name = fields[1]
        last_name = fields[0]
        print(first_name, last_name)
    file.close()

def average(filename, column):
    with open(filename) as file:
        header = next(file)
        header_field = header.strip().split(',') 
        grade_item = header_field[column]
        sum = 0
        count = 0
        for line in file:
            fields = line.strip().split(',')
            score = float(fields[column])  
            sum += score
            count += 1
    average = sum / count
    print(grade_item, "Average is", average)

def plot_grades(filename, column):
    with open(filename) as file: #file = open
        header = next(file)
        header_field = header.strip().split(',') 
        grade_item = header_field[column]
        next(file)
        plotter.init(grade_item + " Grades", "students", "scores")
        for line in file:
            fields = line.strip().split(',')
            score = float(fields[column])
            plotter.add_data_point(score)
        plotter.plot()
        input("Enter to quit")
        

def main():
    # filepath = 'data/numbers_01.txt'
    # print_lines(filepath)
    # word_search('data/words.txt')
    # longest_words('data/words.txt')
    # print_names('data/grades_010.csv')
    # average('data/grades_010.csv', 3)

    # plotter.init("My graph", "x-axis", "y-axis")
    # plotter.add_data_point(75)
    # plotter.add_data_point(90)
    # plotter.add_data_point(60)

    # plotter.plot()
    # plotter.new_series()

    # plotter.add_data_point(60)
    # plotter.add_data_point(50)
    # plotter.add_data_point(70)


    # plotter.plot()

    plot_grades('data/grades_010.csv', 3)


main()