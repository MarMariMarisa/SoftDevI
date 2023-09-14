MAX_FUEL = 15
MPG = 30
class Car:
    __slots__ = ['__vin',"__make","__model","__year","__mileage","__fuel"]
    def __init__(self,vin,make,model,year):
        self.__vin = vin
        self.__make = make
        self.__model = model
        self.__year = year
        self.__mileage = 0.0
        self.__fuel = 0

    def print_car(self):
        print("Car:","vin =",self.__vin,", make =",self.__make,", model = ",self.__model,
        ", year =",self.__year,", mileage=",self.__mileage,", fuel=",self.__fuel)

    def filler_up(self,gallons):
        self.__fuel += gallons
        if self.__fuel > MAX_FUEL:
            self.__fuel = MAX_FUEL

    def drive(self,miles):
        max_miles = self.__fuel * MPG
        if miles > max_miles:
            miles = max_miles
        self.__mileage  += miles
        self.__fuel -= miles/MPG

    def __repr__(self): # repr(car1) -> car1.__repr__()
        return "Car: \n" + \
            "\tvin = " + self.__vin +"\n"+\
                "\tmake = " +self.__make + "\n" + \
                    "\tmodel = " + self.__model + "\n" + \
                        "\tyear = " + str(self.__year) + "\n" + \
                            "\tmileage = " + str(self.__mileage) + "\n" + \
                                "\tfuel = " + str(self.__fuel)

    def __str__(self):
        return "Car: \n" + \
            "\tvin = " + self.__vin +"\n"+\
                "\tmake = " +self.__make + "\n" + \
                    "\tmodel = " + self.__model + "\n" + \
                        "\tyear = " + str(self.__year) + "\n" + \
                            "\tmileage = " + str(self.__mileage) + "\n" + \
                                "\tfuel = " + str(self.__fuel)

    def __eq__(self,other):
        if type(self) != type(other):
            return False
        return self.__vin == other.__vin

    def __ne__(self,other):
        return not self.__eq__(other)

    def __lt__(self,other):
        if type(self) != type(other):
            return False
        return self.__vin < other.__vin
    def __le__(self,other):
        if type(self) != type(other):
            return False
        return self.__vin <= other.__vin
    def __gt__(self,other):
        if type(self) != type(other):
            return False
        return self.__vin > other.__vin
    def __ge__(self,other):
        if type(self) != type(other):
            return False
        return self.__vin >= other.__vin
    def __hash__(self):
         return hash(self.__vin)

