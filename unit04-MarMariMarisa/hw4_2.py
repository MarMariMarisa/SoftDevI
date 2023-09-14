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
        turtle.left(90)
        sides_drawn += 1
    turtle.forward(PIXEL_SIZE * 0.5)
    turtle.end_fill()
    # turtle.forward(PIXEL_SIZE)
def main():
    initalize()
    turtle.speed(3)
    draw_pixel('yellow')
    turtle.write("B", align = 'center', font=("Arial", 19,"normal"))
    input("Enter to quit")
main()