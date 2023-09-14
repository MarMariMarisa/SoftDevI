from tkinter import Y
import pixart
import turtle
#USE PIXART TO MOVE TO TOP LEFT
pixart.initalize()
colCount = 0
rowCount = 0
#this function obtains the single color from a string of color inputs
def get_color(string, index):
    a = ""
    output = ""
    while a != "," :
        output = output + a
        if index == len(string):
            break
        a = string[index]
        index += 1
    return output
#draws a row of pixels based off of inputs of color from user
def draw_row(colors):
    x = colCount
    pixelCounter = 0
    while len(colors) > x:
        y = get_color(clolors, x)
        if pixart.COLUMNS > pixelCounter:
            pixart.draw_pixel(y)
        x = x + len(y) + 1
        pixelCounter += 1
def main():
#prompts user to input colors
    y = rowCount
    while y < pixart.ROWS and y < pixart.COLUMNS:
        x = input("Please enter colors for row:")
        pixart.move(y,colCount - 1)
        draw_row(x)
        y += 1
        turtle.penup()
    input("Enter to close")
main()

