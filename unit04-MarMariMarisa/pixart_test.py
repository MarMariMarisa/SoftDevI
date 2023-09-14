import turtle
import pixart
import math
def assertle(x,y, fillcolor):
    assert turtle.speed() == 0
    assert math.isclose(turtle.xcor(), x)
    assert math.isclose(turtle.ycor(),y)
    assert turtle.isdown()== False
    assert turtle.pencolor()== "black"
    assert turtle.fillcolor() == fillcolor

def test_initalize():
    pixart.initalize()
    assertle(-300,300,"white") 

def test_draw_pixel():
    pixart.draw_pixel("red")
    assertle(-270,300,"red")
    assert turtle.speed()== 0

def test_move():
    pixart.move(5, 4)
    assert turtle.xcor() == -180
    assert turtle.ycor() == 150

def test_draw_row():
    pixart.draw_row(5,4,8)
    assertle(60,150,'red')

def test_draw_square():
    pixart.draw_square(4,5,8)
    assertle(90,-30,'green')

def test_draw_rectangle():
    pixart.draw_rectangle(4,5,6,10)
    assertle(150,30, 'orange')
    
