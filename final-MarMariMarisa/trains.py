import node_stack
import array_queue
"""
Problem 01: 30 Points

A product has a product code (e.g. "ABCD-1234") and a name (e.g. "Washing 
Machine"). 

A partially completed product class has been provided to you below. You must 
complete the class by making the following enhancements:
- Write accessors for all fields.
- Two products are considered equal if they have the same product code.
- Products should be capable of being used with hashing data structures.
- The string representation of a product is its product code with the name in
  parentheses, e.g. "ABCD-1234 (Washing Machine)"
- Products can be sorted based on the product code.

A pytest as been provided to you. Test your code by uncommenting the tests one
at a time! Once you are sure that one test is passing, start on the next test.
"""
class Product:
    __slots__ = ["__product_code", "__name"]

    def __init__(self, product_code, name):
        self.__product_code = product_code
        self.__name = name
    def get_product_code(self):
      return self.__product_code
    def get_name(self):
      return self.__name
    def __eq__(self,other):
      if type(self) != type(other):
        return False
      else:
        return self.__product_code == other.__product_code
    def __hash__(self):
      return hash(self.__product_code)
    def __repr__(self):
      return str(self.__product_code) + " (" + str(self.__name) + ")"
    def __lt__(self,other):
      return self.__product_code < other.__product_code
    
"""
Problem 02: 25 Points

Trains are used to move products across the country by rail. Different train 
cars may have capacity to store different numbers of products. For example, a 
train car with a capcity of 10 can store up to 10 products. Don't worry about
the data structure to store products on the train car just yet - you will be
handling that in the next problem.

Begin implementing a Python class to represent a train car. Make sure to meet 
the following requirements:
- Write a constructor that creates a train car with a specific capacity.
- Use proper encapsulation and write accessors for any fields.
- Write a method that returns True if the train car is empty, and False 
  otherwise. For now, just return True.
- Write a method that returns True if the train car is full, and False 
  otherwise. For now, just return False.
- The string representation of an empty train car is "[]".
- Use the the provided trains_test.py pytest to verify that your class is being
  initialized properly.
"""
"""
class TrainCar:
  __slots__ = ["__capacity"]
  def __init__(self,capacity):
    self.__capacity = capacity
  def get_capacity(self):
    return self.__capacity
  def is_empty(self):
    return True
  def is_full(self):
    return False
  def __repr__(self):
    return "[]"
    """
"""
Problem 03: 25 Points

Train cars are loaded through a door in the back. Products are placed as far
towards the front of the train car as possible, behind any products that were 
loaded previously. Train cars are unloaded through the same door at the back
of the train, beginning with the products closest to the door. This means that
the last product loaded is the first to be unloaded. 

Make the following enhancements to your train car class:
- Choose an appropriate data structure to store the products in the train car.
  Add a field and initialize the empty data structure in your constructor. 
- Implement a method to load a product onto the train car. If the train car is
  full, i.e. the number of products loaded is equal to its capacity, raise a 
  ValueError.
- Implement a method to unload a product from the train car. Remember, the last
  product loaded is the first to be unloaded! If the train car is empty, raise 
  a ValueError.
- Make sure to update the string representation of your train car! It should
  return a comma-separated list of products that have been loaded onto the
  train with the last product first, e.g.:
  "[ABCD-1234 (Washing Machine), XYZQ-5422 (Microwave Oven)]". 
  Hint: can you use the data structure's own string representation?
- Make sure your is_empty and is_full functions are working properly!
- Use the provided pytest to verify your solution!
"""

class TrainCar:
  __slots__ = ["__capacity", "__products"]
  def __init__(self,capacity):
    self.__capacity = capacity
    self.__products = node_stack.Stack()

  def get_capacity(self):
    return self.__capacity
  def is_empty(self):
    return self.__products.is_empty() == True
  def is_full(self):
    return self.__products.size() == self.__capacity
  def __repr__(self):
    string = "["
    hold = self.__products
    while hold.is_empty() == False:
      item = hold.pop()
      string = string + str(item)
      if hold.size() > 0:
        string = string + ", "

    string = string + "]"
    return string
  def load(self,product):
    if self.is_full() == False:
      self.__products.push(product)
    else:
      raise ValueError
  def unload(self):
    if self.is_empty() == True:
      raise ValueError
    else:
      return self.__products.pop()

    

"""
Problem 4: 10 Points

A train comrpises enough train cars to move a shipment of products. As each 
train car is loaded to capacity, it is attached to the end of the train. The
train car at the front of the train is the first that was loaded, and the train
car at the back of the train is the last that was loaded.

When a train arrives at its destination, the train cars are unloaded front to
back - the train car at the front is unloaded first, and the train car at the
back is unloaded last.

Using the description above, choose the best data structure to represent a 
train. Implement a function that, given a shipment of products and the capacity
of the train cars in the train, loads the products onto train cars and stores
the cars in your data structure. Don't forget to return the data structure!

Use the tests in the provided pytest to make sure that your function is working
properly.
"""

def load_train(shipment, capacity):
    train = array_queue.Queue()
    while len(shipment) != 0:
      train_car = TrainCar(capacity)
      for _ in range(0,capacity):
        while train_car.is_full() != True and len(shipment) != 0:
          train_car.load(shipment.pop(0))
      train.enqueue(train_car)
    return train
      


"""
Problem 5: 10 Points

Implement a function that, given a data structure representing a train, 
unloads the products from the train returns them as a list. The products in the
list should be in the same order that they were unloaded.

Use the tests in the provided pytest to make sure that your function is working
properly.
"""
def unload_train(train):
    a_list = []
    while train.size() > 0:
      train_car = train.dequeue()
      while train_car.is_empty() == False:
        product = train_car.unload()
        a_list.append(product)
    return a_list

  
    