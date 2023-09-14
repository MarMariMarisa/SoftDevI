import node
class Stack:
    __slots__ = ["__top","__size"]
    def __init__(self):
        self.__top = None
        self.__size = 0
    def size(self):
        return self.__size
    def in_empty(self):
        return self.__top == None
    def __repr__(self):
        pass
    def push(self,value):
        new_node = node.Node(value,self.__top)
        self.__top = new_node
        self.__size += 1
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is Empty")
        else:
            return self.__top.get_value()