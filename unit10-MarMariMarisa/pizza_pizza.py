class Topping:
    __slots__ = ["price","type","name","order_code"]
    def __init__(self,price,type,name,order_code):
        self.price = price
        self.type = type
        self.name = name
        self.order_code = order_code

class Pizza:
    __slots__ = ["cheese","meat","veggies"]
    def __init__(self,cheese,meat,veggies):
        self.cheese = cheese
        self.meat = meat
        self.veggies = veggies

#insantiate cheeses
FRESH_MOZZARELLA = Topping(1.00,"cheese","Fresh Mozzarella","f")
SHREEDED_CHEESE = Topping(0.00,"cheese","Shredded Cheese","s")
CHEDDER = Topping(0.50,"cheese","Chedder","c")
#insantiate meats
PEPPERONI = Topping(1.50,"meat","Pepperoni","p")
SAUSAGE = Topping(1.50,"meat","Sausage","s")
BACON = Topping(1.00,"meat","Bacon","b")
MEATBALL = Topping(2.00,"meat","Meatball","m")
NONE = Topping(0.00,"meat","none","n")
#insantiate veggies
MUSHROOMS = Topping(1.00,"veggies","Mushrooms","m")
BELL_PEPPERS = Topping(1.00,"veggies","Bell Peppers","b")
JALAPENO_PEPPERS = Topping(1.00,"veggies","Jalapeno Peppers","j")
PINEAPPLE = Topping(1.50,"veggies","Pineapple","p")
NONE = Topping(0.00,"veggies","none","n")
#topping dictionarys
CHEESE_DICTIONARY = {"f": FRESH_MOZZARELLA,
                     "s": SHREEDED_CHEESE,
                     "c": CHEDDER}
MEAT_DICTIONARY = {"p": PEPPERONI,
                   "s": SAUSAGE,
                   "b": BACON,
                   "m": MEATBALL,
                   "n": NONE}
VEGGIES_DICTIONARY = {"m": MUSHROOMS,
                      "b": BELL_PEPPERS,
                      "j": JALAPENO_PEPPERS,
                      "P": PINEAPPLE,
                      "n": NONE}
TOPPING_DICTIONARY = {"veggies": VEGGIES_DICTIONARY,"meat": MEAT_DICTIONARY,"cheese": CHEESE_DICTIONARY}
                  

def print_options_list(type):
    print(type,"options:")
    for key in TOPPING_DICTIONARY[type]:
        print(TOPPING_DICTIONARY[type][key].name,"(",TOPPING_DICTIONARY[type][key].order_code,"): $",TOPPING_DICTIONARY[type][key].price, sep = "",end = " ")

def add_topping_to_pizza(topping,pizza):
    pizza.price += topping.price
    # pizza.topping.type = pizza.topping.type.append()

def build_a_pizza():

    cheese_selected = False
    while cheese_selected == False:
        x = input("choose one type of cheese (0 for options): ")
        if x == 0:
            print_options_list("cheese")
        else:
            #check to make sure selection is valid if selection is valid continue and set
            #cheese_seleced to true
            pass
    
    meat_selected = False
    while meat_selected == False:
        x = input("choose meat option or none(0 for options): ")
        if x == 0:
            print_options_list("meat")
        else:
            #check to make sure selection is valid if selection is valid continue and set
            #cheese_seleced to true
            pass

    veggie_selected = False
    while veggie_selected == False:
        x = input("choose veggie options or none(0 for options): ")
        if x == 0:
            print_options_list("veggie")
        else:
            #check to make sure selection is valid if selection is valid continue and set
            #cheese_seleced to true
            pass
    return "This is gonna be a izzaa"1

def main():
    print("Welcome to Pizza Factory, where all orders include two pizzas!")
    print("For your first pizza...")
    pizza_one = build_a_pizza()
    print("For your second pizza...")
    pizza_two = build_a_pizza()



if __name__ == "__main__":
    main()
