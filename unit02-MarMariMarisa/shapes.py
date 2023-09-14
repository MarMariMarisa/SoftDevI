"""
This program prompts the user for various inputs to calculate the area and volumes of differnt shapes
Author: Marisa Ortiz
"""
#Creating a variable of pi
pi = 3.1415926535

#Area of a circle
def areaOfCircle():
    radius = float(input("Please enter the radius of your circle: "))
    area = pi * radius ** 2
    print("The area of a circle with a radius of", radius, "is", area)
#Calculate the volume of sphere
def volumeOfSphere():
    radius = float(input("Please enter the radius of your sphere: "))
    volume = (4/3) * pi * radius ** 3
    print("The volume of a sphere with a radius of", radius,"is", volume)
#Area of a rectangle
def areaOfARectangle():
    height = float(input("Please enter the height of your rectangle: "))
    width = float(input("Please enter the width of your rectangle: "))
    area = width * height
    print("The area of a rectangle with a height of", height,"and a width of", width, "is", area)
#Area of a square
def areaOfASquare():
    side = float(input("Please enter the side length of your square: "))
    area = side * side
    print("The area of a square with a side length of", side, "is", area)
#Area of an isosceles
def isosceles():
    leg = float(input("Please enter the leg length of your isosceles triangle: "))
    height = float(input("Please enter the height of your isolceles triangle: "))
    base = ((2 *((leg**2) - (height ** 2)) ** 0.5))
    area = (((1/2) * base) * height)
    print("The area of your isosceles triangle with a leg length of", leg, "and a height of", height, "is", area)
#Area of an equilateral
def equilateral():
    length = float(input("Please ther the side length of your equilateral triangle: "))
    area = ((3 ** 0.5)/4) * length ** 2
    print("The area of an equilateral triangle with a side length of", length, "is", area)
#Area of a trapezoid
def trapezoid():
    baseOne = float(input("Please enter base one of your trapezoid: "))
    baseTwo = float(input("Please enter base two of your trapezoid: "))
    height = float(input("Please enter the height of your trapezoid: "))
    area = ((baseOne + baseTwo) / 2) * height
    print("The area of a trapezoid with bases of", baseOne, "and", baseTwo, "is", area)

#Call the functions
def main():

    areaOfCircle()
    volumeOfSphere()
    areaOfARectangle()
    areaOfASquare()
    isosceles()
    equilateral()
    trapezoid()
main()