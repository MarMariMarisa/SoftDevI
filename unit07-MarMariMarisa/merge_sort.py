import arrays
import array_utils
def merge_sort(an_array):
    if len(an_array) <= 1: # base case
        return an_array
    # 1. Divide - Split
    half1, half2 = split(an_array)
    # 2. Conquer - Recursive Call
    sorted_half1 = merge_sort(half1)
    sorted_half2 = merge_sort(half2)
    # 3. Combine - Merge
    sorted_array = merge(sorted_half1,sorted_half2)
    return sorted_array

def split(an_array):
    length = len(an_array)
    half1 = arrays.Array((length + 1) // 2)
    half2 = arrays.Array(length//2)

    for index in range(length):
        if index % 2 == 0:
            half1[index // 2] = an_array[index]
        else:
            half2[index // 2] = an_array[index]
    return half1,half2

def merge(sorted_half1,sorted_half2):
    merged_array = arrays.Array(len(sorted_half1) + len(sorted_half2))
    i1 = 0
    i2 = 0
    i = 0

    while i1 < len(sorted_half1) and i2 < len(sorted_half2):
        if sorted_half1[i1] <= sorted_half2[i2]:
            merged_array[i] = sorted_half1[i1]
            i1 += 1
        else:
            merged_array[i] = sorted_half2[i2]
            i2 += 1
        i += 1

        if i1 == len(sorted_half1):
            while i2 < len(sorted_half2):
                merged_array[i] = sorted_half2[i2]
                i2 += 1
                i += 1
        elif i2 == len(sorted_half2):
            while i1 < len(sorted_half1):
                merged_array[i] = sorted_half1[i1]
                i1 +=1
                i += 1
    return merged_array


def main():
    # sorted_half1 = array_utils.range_array(0,10,2)
    # print(sorted_half1)
    # sorted_half2 = array_utils.range_array(1,10,2)
    # print(sorted_half2)
    # print(merge(sorted_half1,sorted_half2))
    an_array = array_utils.random_array(10,0,10)
    print(an_array)
    print(merge_sort(an_array))

if __name__ == '__main__':
    main()