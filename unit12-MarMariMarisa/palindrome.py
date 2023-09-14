import list_stack
def make_palindrome(a_string):
    palindrome = ""
    a = 0
    word_stack = list_stack.Stack()
    for value in a_string:
        word_stack.push(value)
    for value in reversed(a_string):
        if a == 0:
            a+= 1
            if word_stack.peek().lower() == "a" or word_stack.peek().lower() == "e" or word_stack.peek().lower() == "i"  or str(word_stack.peek()).lower() == 'o' or word_stack.peek().lower() == "a":
                pass
            else:
                word_stack.push(value)
        else:
            word_stack.push(value)
    for elt in word_stack.get_stack():
        palindrome = palindrome + str(elt)
    return palindrome

def main():
    print(make_palindrome("hello"))
    print(make_palindrome("bad"))

if __name__ == "__main__":
    main()
