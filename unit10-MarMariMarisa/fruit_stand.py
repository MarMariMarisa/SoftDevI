class Fruit:
    type = 'fruit'
    price = 0.0
    __slots__ = ["type","price"]
    def __init__(self,type,price):
        self.type = type
        self.price = price

APPLE = Fruit("apple",1.35)
PEAR = Fruit("pear",1.99)
GRAPE = Fruit("grape",2.50)

def print_fruit(a_fruit):
    print("Fruit: ",a_fruit.type,a_fruit.price)

def add_to_basket(basket,selection):
    if selection == 'apple':
        basket.append(APPLE)
    elif selection == 'pear':
        basket.append(PEAR)
    elif selection == 'grape':
        basket.append(GRAPE)
    else:
        print("No",selection)
    return basket

def total_price(basket):
    total_price = 0
    for fruit in basket:
        total_price += Fruit.price
    return total_price

def count_fruit(basket,fruit):
    count = 0
    for fruit in basket:
        count += 1
    for item in basket:
        if item in basket:
            print_fruit(item)
def main():
    # print_fruits(APPLE)
    # print_fruits(PEAR)
    # print_fruits(GRAPE)

    basket = []
    while True:
        selection = input("Select Fruit: ") #apple, pear,grape
        if selection == "":
            break
        add_to_basket(basket,selection)

    #print basket
    print("Basket is printing")
    for item in basket:
        print_fruit(item)

    #paying
    print("Paying ","$",total_price(basket),sep = "")

    print("There are",count_fruit(basket,PEAR))
    print("There are",count_fruit(basket,GRAPE))
    print("There are",count_fruit(basket,APPLE))

if __name__ == "__main__":
    main()
