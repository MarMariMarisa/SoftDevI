import cross_maker
import turtle
PIXEL_SIZE = 30
ROWS = 16
COLUMNS = 16
def test_draw_pixel_with_letter():
    #setup
    color = "Purple"
    letter = "A"
    row = 3
    col = 3
    #invoke
    cross_maker.draw_pixel_with_letter(color, letter, row, col)
def test_valid_tester_is_valid():
    #setup
    word = "Hello"
    col = 2
    row = 3
    is_horizontial = True
    expected = True
    #invoke
    actual = cross_maker.validate_word(word,row,col,is_horizontial)
    # analyze
    assert expected == actual
def test_valid_tester_not_valid():
     #setup
    word = "Hello"
    col = 15
    row = 3
    is_horizontial = True
    expected = False
    #invoke
    actual = cross_maker.validate_word(word,row,col,is_horizontial)
    # analyze
    assert expected == actual
def test_token_splitting():
    #setup
    string = "15 12 Hello h"
    expected = "h"
    #invoke
    actual = cross_maker.split_input(string,3)
    assert expected == actual
def test_draw_word_vertical():
    #setup
    string = "Hello World!"
    #invoke
    cross_maker.draw_word(3,3,string, False)
def test_draw_word_hotizontial():
    #setup
    string = "Hello World!"
    #invoke
    cross_maker.draw_word(3,3,string, True)
def test_combine_functions():
    string = "3 3 Hello v"
    cross_maker.combine_functions(string)
def test_prompt_user():
    cross_maker.prompt_user()
#test_draw_word_vertical()
#test_draw_word_hotizontial()
#test_combine_functions()
test_prompt_user()


