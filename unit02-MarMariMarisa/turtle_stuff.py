import turtle
def square():
    # pen down, facing east, (0,0)
    turtle.forward(100)
    turtle.right(90) # facing south
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
def test_drive():
    turtle.forward(100)
    turtle.setheading(270)
    turtle.circle(200, 90)
    turtle.up()
    turtle.goto(-200,300)
    turtle.down()
def turtle_state():
    print("pen down?:", turtle.isdown())
    print("heading:", turtle.heading())
    print("Positon:", turtle.xcor(),turtle.ycor())
def main():
    turtle_state()
    test_drive()
    turtle_state() 
    test_drive()
    turtle_state()
    square()
    input("Enter to quit: ")


main()
    