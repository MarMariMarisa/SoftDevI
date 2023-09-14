import array
import array_utils
def max(an_array,index = 0,maximum = None):
    if index == 0:
        maximum = an_array[0]
    elif len(an_array) == 0:
        return None
    elif index >= len(an_array):
        """
        I am very comfused here. I am attempting to return my maximum
        value however it is reutrning none insteadwhen it should be
        returning the max however if i try to print maximum instead of 
        returning it prints the correct number why is my maximum printing 
        differnt then it is returning? :(
        """
        return maximum
    else:
        if an_array[index] > maximum:
            maximum = an_array[index]
        return max(an_array,index + 1,maximum)

def power(base,exponent):
    if exponent < 0:
        return "Undefined"
    elif exponent == 0:
        return 1
    elif exponent % 2 == 1:
        return base * power(base,exponent // 2) * power(base,exponent//2)
    elif exponent % 2 == 0:
        return power(base,exponent // 2) * power(base,exponent //2)


def main():
    an_array = array_utils.range_array(0,10)
    print(max(an_array))

    result = power(4,7)
    print(result)

if __name__ == "__main__":
   main ()

        
    