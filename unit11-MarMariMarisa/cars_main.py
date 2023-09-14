import cars

def main():
    car1 = cars.Car("ABC","Toyota","Lexus",2002)
    car2 = cars.Car("ZZZ","Ford","Focus",2010)
    car3 = cars.Car("AAA","Ford","Focus",2010)
    # list_cars = [car1,car2,car3]
    # list_cars.sort()
    # print(list_cars)
    set_cars = set()
    set_cars.add(car1)
    set_cars.add(car2)
    set_cars.add(car3)
    print(set_cars)
    # print(car1 == car2)
    # print(car1 != car2)
    # print(car1)
    # print(str(car1))
    # print(repr(car1))
    # car1.print_car()
    # car2.print_car()
    # car1.filler_up(5)
    # car1.print_car()

    # car1.drive(200)
    # car1.print_car()

main()

