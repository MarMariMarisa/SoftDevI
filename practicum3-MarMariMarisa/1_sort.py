def swap(a_array, i, j):
    temp = a_array[i]
    a_array[i] =a_array[j]
    a_array[j] = temp

def insertion_sort_backward(a_array):
    for index in range(len(a_array)-1,-1,-1):
        shift_backwards(a_array,index)

def shift_backwards(an_array,index):
    while index >= 0 and len(an_array) - 1 > index and an_array[index+1] < an_array[index]:
        swap(an_array,index,index+1)
        index += 1
def main():
    a_array = [5,3,7,1,4]
    insertion_sort_backward(a_array)
    print(a_array)

main()