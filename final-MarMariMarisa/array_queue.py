import arrays

class Queue:
    __slots__ = ['__size', '__front', '__back', '__array']
    def __init__(self, capacity = 3):
        self.__size = 0
        self.__front = 0
        self.__back = 0 # the index for the next to be enqueued
        self.__array = arrays.Array(capacity)
    
    def size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0
    
    def __repr__(self):  # [z, None, x, y], back = 1, front = 2
        i = self.__front
        string = ""
        for _ in range(self.__size):
            string = string + str(self.__array[i]) + ", "
            i = (i+1)%len(self.__array)
        return "[" + string[:-2] + "]"
    
    def _resize(self):
        new_array = arrays.Array(len(self.__array)*2)
        i = self.__front
        j = 0
        for _ in range(len(self.__array)):
            new_array[j] = self.__array[i]
            i = (i + 1) % len(self.__array)
            j = j + 1
        self.__front = 0
        self.__back = j
        self.__array = new_array
        

    def enqueue(self, value):
        self.__array[self.__back] = value
        self.__back = (self.__back + 1) % len(self.__array)
        self.__size += 1

        if self.__front == self.__back:
            # print("Array is full. No more elements!")
            self._resize()

    def front(self):
        if self.is_empty():
            raise IndexError("front on an empty queue")
        return self.__array[self.__front]
    
    def back(self):
        if self.is_empty():
            raise IndexError("front on an empty queue")
        return self.__array[(self.__back-1)% len(self.__array)]
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("front on an empty queue")
        dequeued = self.__array[self.__front]
        self.__front = (self.__front + 1) % len(self.__array)
        self.__size -= 1
        return dequeued


def main():
    queue = Queue()
    queue.enqueue('a')
    queue.enqueue('b')
    print(queue.dequeue()) # a
    queue.enqueue('c')
    queue.enqueue('d')
    queue.enqueue('e')
    print(queue)

if __name__ == '__main__':
    main()

    


