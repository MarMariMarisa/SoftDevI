import Boolean
def assertTest(gr1,gr2,let):
    #setup
    grade1 = gr1
    grade2 = gr2
    expected = let
    #invoke
    actual = Boolean.grade(grade1,grade2)
    assert actual == expected

def test_grade_A():
    assertTest(90,92,"A")

def test_grade_B():
    assertTest(100,82,"B")

def test_grade_C():
    assertTest(72,90,"C")

def test_grade_D():
    assertTest(100,69,"D")

def test_grade_F():
    assertTest(100,50,"F")

def main():
    test_grade_A()
    test_grade_B()
    test_grade_C()
    test_grade_D()
    test_grade_F()
main()