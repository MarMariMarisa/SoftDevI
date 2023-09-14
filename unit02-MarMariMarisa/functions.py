from turtle import bye
"""
This program calculates the users age in months
Author: Marisa Ortiz

"""
def ageInMonths():
    """
    Prompt the user for inputs
    """
    year = int(input("Current Year: "))
    month =int(input("Current Month(Numerically): "))
    bYear = int(input("Birth Year: "))
    bMonth = int(input("Please enter your birth month(Numerically): "))
    """
    Calculate the age in months
    """
    ageInMonths = 12 * (year - bYear) + (month - bMonth)
    """
    Print the age in months
    """
    print("Your age in months:", ageInMonths)


def main():
    ageInMonths()


main()



