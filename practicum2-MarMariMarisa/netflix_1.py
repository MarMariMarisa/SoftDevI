import csv
import time
"""

You have been asked to help exlore the data files used in the annual Netflix data mining competition.
The competition uses remarkably simple data as training data for statistical agents. You have one
of those files in your data folder: a ratings file (partial_data2.txt). You can inspect it in an editor or VS Code.

The ratings file consists of an index (not used) with a colon and on the remaining lines rows of ratings in the format:

index:
client id, rating, date of rating

1:
2590061,3,2004-08-12 <- client id, rating, date
2442,3,2004-04-14
543865,4,2004-05-28
1209119,4,2004-03-2
...

Write a function calculate_ratings to count and return how many ratings exist along with the average rating.
The function declares a parameter for the file name. 
Use exception handling to prevent your code from crashing on unexpected lines.

Hints: 
-- You can use next(f) to skip lines in the file.
-- If file contains a line with bad data, return with the data collected so far.

Bonus:
-- Implement reading the file using csv. All the requirements remain the same.

"""

def count_ratings(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        rating_count = 0
        average = 0
        counter = 0
        for record in csv_reader:
                rating_count += 1
                try:
                    counter = counter + int(record[1])
                except:
                    average = counter / rating_count
                    print("Error in data")
                    return rating_count,average
        average = counter / rating_count
        return rating_count,average


def main():
    ratings, average = count_ratings("data/partial_data2.txt")
    print ("Total ratings =", ratings, "Average rating =", average)

if __name__ == "__main__":
    main()
