import math
class Circle:
    __slots__ = ['__center', '__radius']
    def __init__(self,center,radius):
        self.__center = center
        self.__radius = radius

    def __repr__(self):
        return "Center: " + str(self.__center) + " Radius: " + str(self.__radius)
    
    def __lt__(self,other):
        return self.__radius < other.__radius
    
    def __gt__(self,other):
        return self.__radius > other.__radius
    def intersect(self,other):
        x_1 = self.__center[0]
        x_2 = other.__center[0]
        y_1 = self.__center[1]
        y_2 = other.__center[1]
        if self.__radius + other.__radius > math.sqrt((x_1-x_2)**2 + (y_1-y_2)**2):
            return True
        else:
            return False
def main():
    circle1 = Circle((0, 0), 2)
    circle2 = Circle((4, 0), 3) 
    circle3 = Circle((3, 3), 1)
    a_list = [circle1, circle2, circle3]
    a_list.sort()
    print(a_list)
    print("circle1 and circle2 intersect:", circle1.intersect(circle2)) # True
    print("circle1 and circle3 intersect:", circle1.intersect(circle3)) # False
    print("circle2 and circle3 intersect:", circle2.intersect(circle3)) # True

main()           
    
