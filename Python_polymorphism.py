# Funtion Overiding in Python

# Import math Library
from math import pi

class Shape:

    # Constructor 
    def __init__(self, name):
        self.name = name

    # Methods
    def area(self):
        pass

    def fact(self):
        pass
    
    def whichShape(self):
        print("Shape : {}".format(self.name))


class Square(Shape):
    # Constructor
    def __init__(self, name, length):
        super().__init__(name)
        self.sideLength = length

    # Method Overriding
    def area(self):
        area = self.sideLength ** 2
        print("Area : {}".format(area))

    def fact(self):
        print("Square has each angle equal to 90 Degrees")


class Circle(Shape):

    # Constructor
    def __init__(self, name, radius):
        super().__init__(name)
        self.circleRadius = radius

    # Method Overriding
    def area(self):
        area = pi * (self.circleRadius ** 2)
        print("Area : {}".format(area))

# Creating Objects
sq = Square("Sqaure", 5)
cr = Circle("Circle", 3)

sq.area()
cr.area()

sq.fact()
cr.fact()

sq.whichShape()
cr.whichShape()