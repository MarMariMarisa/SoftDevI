import array_utils

"""
A linear search searches an array index by index. 
If the target value is found, the index is returned. 
Otherwise the function returns None.

Define a function named linear_search_rec that declares 
parameters for an_array and the target value.
Your function should implement a linear search using recursion. 
You may add additional parameters as needed.

A linear search function using iteration is provided below for your reference.

Test your function from main by creating an array containing values 
from 0 to 10 and searching for values 0, 5, and 20.
"""

def linear_search_iter(an_array, target):
    for index in range(len(an_array)):
        if an_array[index] == target:
            return index
    return None

def linear_search_rec(an_array, target, index = 0):
    #base case
    if index >= len(an_array):
        return None
    elif an_array[index] == target:
        """
        Im having the same problem I had in the mini practicum
        where I attempt to reutrn a number and it returns none when it
        should not be and the number does exist

        When I print index it prints correctly as 5 but when I return it returns 
        as none 
        :(
        """
        print(index)
        return index
     #single unit of work
    else:
        linear_search_rec(an_array,target,index+1)

def main():
    an_array = array_utils.range_array(0,11)
    print(linear_search_rec(an_array,0))
    print(linear_search_rec(an_array,5))
    print(linear_search_rec(an_array,20))

main()


