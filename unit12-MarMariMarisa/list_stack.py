class Stack:
    __slots__ = ["__top","__size"]
    def __init__(self):
        self.__top = [] #right end as the top of stack
        self.__size = 0
    def get_stack(self):
        return self.__top
    def push(self,value):
        self.__top.append(value)
        self.__size +=1
    def pop(self):
        self.__size -= 1
        return self.__top.pop() #pops rightmost value aka top of the stack
    def peek(self):
        return str(self.__top[len(self.__top)-1])
    def is_empty(self):
        return len(self.__top) == 0   
    def __repr__(self):
        return str(self.__top)





