class Node:
    __slots__ = ["__value","__next"]
    def __init__(self,value,next=None):
        self.__value = value
        self.__next = next
    def get_value(self):
        return self.__value
    def get_next(self):
        return self.__next

def print_node(node_seq):
    if node_seq is None:
        pass
    else:
        print(node_seq.get_value())
        print_node(node_seq.get_next())

def print_node_iter(node_seq):
    curr_node = node_seq
    while curr_node != None:
        print(curr_node.get_value(),end = " ")
        curr_node = curr_node.get_next()
    print()
def main():
    node1 = Node(10)
    node2 = Node(20,node1)
    head = Node(30,node2)
    print("second node value:",head.get_next().get_value())
    print("third node value:",head.get_next().get_next().get_value())

