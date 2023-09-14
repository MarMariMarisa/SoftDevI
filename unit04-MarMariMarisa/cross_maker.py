from operator import length_hint
import turtle
from tkinter.tix import ROW 
PIXEL_SIZE = 30
ROWS = 16
COLUMNS = 16

def initalize():
    turtle.speed(0)
    turtle.penup()
    x = -COLUMNS / 2 * PIXEL_SIZE
    y = ROWS / 2 * PIXEL_SIZE
    turtle.setpos(x,y)
    turtle.pensize(1)
    turtle.fillcolor("white")
    turtle.pencolor("black")
#this function moves to the location of the
def move(row, col):
    row = int(row)
    col = int(col)
    turtle.up()
    x = -COLUMNS / 2 * PIXEL_SIZE
    y = ROWS / 2 * PIXEL_SIZE
    x = x + col * PIXEL_SIZE
    y = y - row * PIXEL_SIZE
    turtle.setpos(x, y)
#this function draws a single square
def draw_pixel(fillcolor):
    # at top left corner of the pixel
    turtle.fillcolor(fillcolor)
    turtle.begin_fill()
    turtle.pendown()
    sides_drawn = 0
    while sides_drawn < 4:
        turtle.forward(PIXEL_SIZE)
        turtle.left(90)
        sides_drawn += 1
    turtle.forward(PIXEL_SIZE * 0.5)
    turtle.end_fill()
    # turtle.forward(PIXEL_SIZE)
#this function draws a pixel with a letter in it
def draw_pixel_with_letter(fillcolor, letter, row, col):
    row = int(row)
    col = int(col)
    move(row,col)
    draw_pixel(fillcolor)
    turtle.color("white")
    turtle.write(letter, align = 'center', font=("Arial", 19,"normal"))
    turtle.color("black")
# This function returns true or false depending on if the word is valid or not
def validate_word(word,row,col,is_horizontial):
    a = len(word)
    row = int(row)
    col = int(col)
    if is_horizontial == True:
        if row > 0 and row <= ROWS and a + col <= COLUMNS:
            return True
        else:
            return False
    if is_horizontial == False:
        if col > 0 and col <= COLUMNS and a + row <= ROWS:
            return True
        else:
            return False  
#this function splits the input into readable tokens
def split_input(string,id):
    tokens = string.split(" ")
    token = tokens[id]
    return token

# def draw_word(x,y,word,is_horizontial):
def draw_word(x, y, word, is_horizontial):
    x = int(x)
    y = int(y)
    if validate_word(word,y, x, is_horizontial) == False:
        print("Invalid word entered")
    elif validate_word(word,y,x,is_horizontial) == True:
        count = 0
        while count < len(word):
            letter = word[count]
            draw_pixel_with_letter("black",letter,y,x)
            count += 1
            if is_horizontial == True:
                x += 1
            else:
                y += 1

def combine_functions(string):
    y = split_input(string,1)
    x = split_input(string, 0)
    word = split_input(string, 2)
    is_horizontial = split_input(string, 3)
    if is_horizontial == "h":
        is_horizontial = True
    if is_horizontial == "v":
        is_horizontial = False
    draw_word(x,y,word,is_horizontial)

def prompt_user():
    while 0 == 0:
        ui = input("Pleae enter your word in a row col string h/v format: ")
        if ui == "":
            break
        else:
            combine_functions(ui)

def main():
    prompt_user()

main()
