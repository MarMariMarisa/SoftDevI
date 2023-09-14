
import turtle

def a_piece(x, y, radius, color,crust):

    turtle.penup()
    turtle.goto(x,y)
    turtle.fillcolor(crust)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(radius * 1.25)
    turtle.left(90)
    turtle.circle(radius * 1.25, 60)
    turtle.left(90)
    turtle.forward(radius * 1.25)
    turtle.end_fill()
    turtle.right(60)

    turtle.penup()
    turtle.goto(x,y)
    turtle.left(180)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(radius)
    turtle.left(90)
    turtle.circle(radius, 60)
    turtle.left(90)
    turtle.forward(radius)
    turtle.end_fill()
    turtle.left(60)

def six_pieces(x,y,radius,color,crust):
    cnt = 1
    while cnt <= 6:
        a_piece(x,y,radius,color,crust)
        cnt +=1

def six_colorful_pieces(x,y,radius,crust):
    a_piece(x,y,radius,"yellow",crust)
    a_piece(x,y,radius,"pink",crust)
    a_piece(x,y,radius,"red",crust)
    a_piece(x,y,radius,"orange",crust)
    a_piece(x,y,radius,"green",crust)
    a_piece(x,y,radius,"blue",crust)

def a_pizza(x,y,radius,color):
    turtle.up()
    turtle.goto(x,y)
    six_colorful_pieces(x,y,radius,color)


def main():
    turtle.pensize(2)
    a_piece(0,0,60,"purple","yellow")

    turtle.tracer(False)

    # a pizza with radius 200 centered at (100, 100) with gold crust
    a_pizza(100, 100, 200, 'gold') 

    # a pizza with radius 150 centered at (-200, -200) with beige crust
    a_pizza(-200, -200, 150, 'beige')

    # a pizza with radius 100 centered at (200, -200) with yellowgreen crust
    a_pizza(200, -200, 100, 'yellowgreen')


    turtle.tracer(True)
    turtle.hideturtle()
    input("Press enter to quit: ")

main()
