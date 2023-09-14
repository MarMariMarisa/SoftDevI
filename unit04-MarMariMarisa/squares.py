import turtle as t
newL = 0
def draw_squares(side):
    
    t.setheading(0)
    t.penup()
    t.forward(0.5 * side)
    t.fillcolor("red")
    #first square
    t.begin_fill()
    t.pensize(3)
    t.pendown()
    t.left(90)
    t.forward(side * 0.5)
    t.left(90)
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.left(90)
    t.forward(side * 0.5)
    t.end_fill()
    #second square
    def inner_Square(fillcolor, newL):
        t.left(45)
        t.fillcolor(fillcolor)
        t.begin_fill()
        t.forward(newL)
        t.left(90)
        t.forward(newL)
        t.left(90)
        t.forward(newL)
        t.left(90)
        t.forward(newL)
        t.left(90)
        t.forward(newL * 0.5)
        t.end_fill()

    inner_Square("orange", (2 * (0.5 * side) ** 2) ** 0.5 )
    side = (2 * (0.5 * side) ** 2) ** 0.5
    inner_Square("yellow", (2 * (0.5 * side) ** 2) ** 0.5 )
    side = (2 * (0.5 * side) ** 2) ** 0.5
    inner_Square("green",  (2 * (0.5 * side) ** 2) ** 0.5 )
    side = (2 * (0.5 * side) ** 2) ** 0.5
    inner_Square("blue",  (2 * (0.5 * side) ** 2) ** 0.5)
    side = (2 * (0.5 * side) ** 2) ** 0.5
    inner_Square("purple",(2 * (0.5 * side) ** 2) ** 0.5 )

def main():
    draw_squares(500)
    input("Enter to close")
main()