import activity
def test_exponent_no_error():
   #setup
    base = 2
    power = 3
    expected = 8

    #invoke
    actual = activity.exponent(base, power)

    #analyze
    assert expected == actual

def test_exponent_error():
   #setup
    base = 2
    power = -3
    try:
        #invoke
        actual = activity.exponent(base, power)
        # should not come here
        assert False, "Oh no you silly little goose what are you doing here?"
    except:
        #should be here
        assert True, "Silly goose what are you doing!"
    #analyze