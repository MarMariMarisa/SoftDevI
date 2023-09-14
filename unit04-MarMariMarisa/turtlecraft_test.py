import turtlecraft
def test_color_input_multiple():
    #setup
    input = "purple,blue,green"
    indexNum = 7
    expected = "blue"
    #invoke
    actual = turtlecraft.get_color(input,indexNum)
    #analyze
    assert expected == actual

def test_color_input_single():
    #setup
    input = "purple"
    indexNum = 0
    expected = "purple"
    #invoke
    actual = turtlecraft.get_color(input,indexNum)
    #analyze
    assert expected == actual
test_color_input_multiple()
test_color_input_single()
