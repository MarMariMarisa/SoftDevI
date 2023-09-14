PROTOCOL = "Protocol"
ASTROMECH = "Astromech"

PROTOCOL_PARTS = ["p_head", "p_chassis","p_left_arm", "p_right_arm", "p_left_leg","p_right_leg"]
ASTROMECH_PARTS = ["a_dome", "a_body","a_left_leg", "a_center_leg", "a_right_leg"]

class Droid:
    __slots__ = ["__type","__serial_number","__parts"]
    def __init__(self,serial_number,type = PROTOCOL):
        self.__type = type
        self.__serial_number = serial_number
        self.__parts = {}
        if type == PROTOCOL:
            for part in PROTOCOL_PARTS:
                self.__parts[part] = False
        elif type == ASTROMECH:
            for part in ASTROMECH_PARTS:
                self.__parts[part] = False
        else:
            raise TypeError("Invalid droid type " + str(type))

    def needs_part(self,part):
        return part in self.__parts and not self.__parts[part]

    def install(self,part):
        if self.needs_part(part) == True:
            self.__parts[part] = True
        else:
            raise ValueError(str(part) + "not needed")

    def is_complete(self):
        for part in self.__parts:
            if not self.__parts[part]:
                return False
        return True
    
    def __repr__(self):
        string = str(self.__type) + " droid" + "\n" + str(self.__serial_number)
        for part in self.__parts:
            string = string +  "\n\t" + str(part)
            if self.__parts[part]:
                string = string + " Installed"
            else:
                string = string + " Missing"
        return string
    def __str__(self):
        string = str(self.__serial_number)
        if self.is_complete():
            string = string + " Complete"
        else:
            string = string + " Incomplete"
        return string
def main():
    protocol = Droid('C3PO')
    print(protocol.is_complete())
    for part in PROTOCOL_PARTS:
        protocol.install(part)
    print(protocol.is_complete())

    astromech = Droid('C3P2',ASTROMECH)
    print(astromech.is_complete())
    for part in ASTROMECH_PARTS:
        astromech.install(part)
    print(astromech.is_complete())

    
if __name__ == "__main__":
    main()