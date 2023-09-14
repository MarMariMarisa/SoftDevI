import csv
import random
import array_queue
import node_stack
class GroceryItem:
    __slots__ = ["__name","__weight","__price"]
    def __init__(self,name,weight,price):
        self.__name = name
        self.__weight = weight
        self.__price = price

    def get_name(self):
        return self.__name
    def get_weight(self):
        return self.__weight
    def get_price(self):
        return self.__price
    
    def __repr__(self):
        return self.__name + " " + str(self.__weight) + "lb $" + str(self.__price)

    def __eq__(self,other):
        if type(self) == type(other):
            return self.__name == other.__name
        else:
            return False

    def __hash__(self):
        return hash(self.__name)
    def __lt__(self,other):
        if type(self) == type(other):
            return self.__weight < other.__weight
        else:
            raise TypeError("'<' not supported bewteen instances of " + type(self).__name__ + " " + type(other).__name__)
class Customer:
    __slots__ = ["__list","__cart","__bags"]
    def __init__(self,shopping_list):
        self.__list = shopping_list
        self.__cart = set()
        self.__bags = []

    def get_bags(self):
        return self.__bags
    def shop(self,store):
        for item_name in self.__list:
            self.__cart.add(store[item_name])    
    def unload(self,belt):
        for item in belt:
            belt.enqueue(item)

    def checkout(self,belt):
        bag = node_stack.Stack()
        while not belt.is_empty():
            item = belt.dequeue()
            if item.get_weight() < bag.peek().get_weight():
                bag.push(item)
            else:
                bag = node_stack.Stack()
                self.__bags.append(bag)
                bag.push(item)

    def unpack(self):
        count = 1
        for bag in self.__bags:
            print("Unpacking bag #",count)
            while not bag.is_empty():
                item = bag.pag()
                print(" ",item)





def stock_store(filename):
    store = dict()
    with open(filename ) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for record in csv_reader:
            name = record[0]
            weight = int(record[1])
            price = int(record[2])
            item = GroceryItem(name,weight,price)
            store[name] = item
    return store
def main():
    store = stock_store("data/groceries.csv")
    all_item_names = list(store.keys())
    random.shuffle(all_item_names)
    shopping_list = all_item_names[:25]
    
    a_customer = Customer(shopping_list)
    a_customer.shop(store)
    belt = array_queue.Queue()
    a_customer.unload(belt)
    a_customer.checkout(belt)
    
    a_customer.unpack()

main()