
class Pokemon:
    __slots__ = ["__name","__type","__health_points","__damage_points"]
    def __init__(self,name,type,health_points,damage_points):
        self.__name = name
        self.__type = type
        self.__health_points = health_points
        self.__damage_points = damage_points

    def get_damage_points(self):
        return self.__damage_points
    def get_name(self):
        return self.__name
    def get_type(self):
        return self.__type
    def lose_round(self,damage_points):
        self.__health_points = self.__health_points
        self.__health_points = self.__health_points
        self.__health_points -= damage_points

    def is_fainted(self):
        return self.__health_points <= 0

    def __str__(self):
        return self.__name

    def __repr__(self):
        return self.__name + ":" + self.__type + ":" + self.__health_points
    
    def __eq__(self,other):
        if type(self) != type(other):
            return False
        return self.__type == other.__type and self.__health_points == other.__health_points
    
    def __ne__(self,other):
        return not self.__eq__(other)

    def __gt__(self,other):
        #water _> fire grass water
        if type(self) != type(other):
            return False
        if self.__type == "water" and other.__type == "fire":
            return True
        if self.__type == "fire" and other.__type== "grass":
            return True 
        if self.__type == "grass" and other.__type == "water":
            return True
        if self.__type == other.__type:
            return self.__health_points > other.__health_points
        return False
    def __ge__(self,other):
        if type(self) != type(other):
            return False
        if self.__type == "water" and other.__type == "fire":
            return True
        if self.__type == "fire" and other.__type== "grass":
            return True 
        if self.__type == "grass" and other.__type == "water":
            return True
        if self.__type == other.__type:
            return self.__health_points == other.__health_points
        return False
    def __lt__(self,other):
        if type(self) != type(other):
            return False
        if other.__type == "water" and self.__type == "fire":
            return True
        if other.__type == "fire" and self.__type== "grass":
            return True 
        if other.__type == "grass" and self.__type == "water":
            return True 
        if self.__type == other.__type:
            return other.__health_points > self.__health_points
        return False
    def __le__(self,other):
        if type(self) != type(other):
            return False
        if other.__type == "water" and self.__type == "fire":
            return True
        if other.__type == "fire" and self.__type== "grass":
            return True 
        if other.__type == "grass" and self.__type == "water":
            return True 
        if self.__type == other.__type:
            return other.__health_points == self.__health_points
        return False
    def __hash__(self):
        return hash(self.__name)

    

