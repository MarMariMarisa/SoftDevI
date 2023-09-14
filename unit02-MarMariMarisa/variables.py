"""
Variable Practice
author: Marisa Ortiz
"""

from cmath import exp


def variable_practice():
    """
    Declaring the variables
    """
    ageInMonths = "219"
    daysPerYear = "365"
    nameOfFirstPet = "Leo"
    piFirstFive = "3.1415"
    """
    Printing the variables
    """
    print("ageInMonths =",ageInMonths)
    print("daysPerYear =", daysPerYear)
    print("nameOfFirstPet =", nameOfFirstPet)
    print("piFirstFive =", piFirstFive)

def expressions_practice():
    """
    Declaring Variables
    """
    literal = 15
    addition = 2 + 3
    exponent = 2 ** 3
    floor_division = 2//3  #0
    mod = 18 % 4   #18 = 4*4 =2
    quotient = 18 // 4
    parent = (1+2) * 3

    """
    Printing Variables
    """

    print(addition)
    print(literal)
    print(exponent)
    print(floor_division)
    print(mod)
    print(quotient)
    print(parent)

def prompt_print():
    """
    Declaring Variables
    """
    number1 = float(input("Enter your first number: "))
    number2 = float(input("Enter your second number: "))

    """"
    Printing Variables
    """
    print(number1 + number2)
    print(number1 - number2)
    print(number1 * number2)
    print(number1/number2)



#Calling the functions
def main():

    variable_practice() 
    expressions_practice()
    prompt_print()

main()
