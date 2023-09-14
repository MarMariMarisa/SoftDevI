import arrays
import array_utils
import sorts
import math
def quicksort(an_array):
    if len(an_array) <= 1:
        return an_array
    #1. Divide
    else:
        pivot = an_array[0]
        less,same,more = partition(pivot,an_array)
        #2. conquer
        sorted_less = quicksort(less)
        sorted_more = quicksort(more)
        #3. combine
        sorted_less_same = cat(sorted_less,same)
        sorted_array = cat(sorted_less_same,sorted_more)
        return sorted_array
def quick_insertion_sort (an_array, recursions = None):
    if recursions == None:
        recursions = 2*math.log2(len(an_array))

    if len (an_array) < 2:
        return an_array
    elif recursions < 0:
        sorts.insertion_sort(an_array)
        return an_array
    else:
        pivot = an_array[0]
        less, same, more = partition (pivot, an_array)
        sorted_less = quick_insertion_sort(less, recursions-1)
        sorted_more = quick_insertion_sort(more, recursions-1)
        new_array = cat(sorted_less, same)
        new_array = cat (new_array, sorted_more)
        return new_array

def partition(pivot,an_array):
    count_less = 0
    count_same = 0
    count_more = 0
    for i in range(len(an_array)):
        if an_array[i] < pivot:
            count_less += 1
        elif an_array[i] > pivot:
            count_more += 1
        else:
            count_same += 1
    less = arrays.Array(count_less)
    same = arrays.Array(count_same)
    more = arrays.Array(count_more)
    less_index = 0
    same_index = 0
    more_index = 0
    for i in range(len(an_array)):
        if an_array[i] < pivot:
            less[less_index] = an_array[i]
            less_index += 1
        elif an_array[i] > pivot:
            more[more_index] = an_array[i]
            more_index += 1
        else:
            same[same_index] = an_array[i]
            same_index += 1

    return less,same,more

def cat(a,b): #[x,y,z] + [u,v] = [x,y,z,u,v]
    len_a = len(a)
    len_b = len(b)
    an_array = arrays.Array(len_a+len_b)
    for i in range(len_a):
        an_array[i] = a[i]

    for i in range(len_b):
        an_array[i + len_a] = b[i]
    return an_array

def main():
    an_array = array_utils.random_array(10,0,10)
    print(an_array)
    sorted_array = quicksort(an_array)
    print(sorted_array)
    # print(an_array)
    # less,same,more = partition(an_array[0],an_array,)
    # print(less)
    # print(same)
    # print(more)


if __name__ == "__main__":
    main()