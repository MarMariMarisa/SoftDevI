from tkinter.tix import ROW
import turtle

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
def draw_pixel(fillcolor):
    # at top left corner of the pixel
    turtle.fillcolor(fillcolor)
    turtle.begin_fill()
    turtle.pendown()
    sides_drawn = 0
    while sides_drawn < 4:
        turtle.forward(PIXEL_SIZE)
        turtle.right(90)
        sides_drawn += 1
    turtle.end_fill()
    turtle.forward(PIXEL_SIZE)
def move(row, col):
    turtle.up()
    x = -COLUMNS / 2 * PIXEL_SIZE
    y = ROWS / 2 * PIXEL_SIZE
    x = x + col * PIXEL_SIZE
    y = y - row * PIXEL_SIZE
    turtle.setpos(x, y)
def draw_row(row, col, pixels, color = 'red'):
    turtle.penup()
    move(row, col)
    count = 0 # how many pixels
    # while count < pixels:
    #     draw_pixel(color)
    #     count += 1
    for count in range(pixels):
        draw_pixel(color)
def draw_square(row,col,pixels, color = 'green'):
    # move(row, col)
    # for count in range(pixels):
    #     draw_row(row,col,pixels, color)
    #     row += 1
    draw_rectangle(row,col,pixels,pixels,color)
    
def draw_rectangle(row,col,height,width,color = 'orange'):
    move(row,col)
    for count in range(height):
        draw_row(row,col,width,color)
        row += 1

    







