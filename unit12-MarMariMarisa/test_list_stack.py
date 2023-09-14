import list_stack

def test_make_stack():
    a_stack = list_stack.Stack()
    assert a_stack.get_stack() == []

def test_push():
    a_stack = list_stack.Stack()
    a_stack.push(50)
    a_stack.push(40)
    a_stack.push(30)

    assert a_stack.get_stack() == [50,40,30]

def test_pop():
    a_stack = list_stack.Stack()
    a_stack.push(50)
    a_stack.push(40)
    a_stack.push(30)

    a_stack.pop()

    assert a_stack.get_stack() == [50,40]

def test_peek():
    a_stack = list_stack.Stack()
    a_stack.push(50)
    a_stack.push(40)
    a_stack.push(30)
    a_stack.peek() == 30

def test_is_empty():
    a_stack = list_stack.Stack()
    assert a_stack.is_empty() == True
    a_stack.push(50)
    a_stack.is_empty() == False

def test_repr():
    a_stack = list_stack.Stack()
    a_stack.push(50)
    a_stack.push(40)
    a_stack.push(30)
    assert str(a_stack) == "[50, 40, 30]"
