from math import sqrt


class Triangle():
    def __init__(self, side1 = 1, side2 = 1, side3 = 1):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def getSides(self):
        return self.side1, self.side2, self.side3
    
    def getArea(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return sqrt((s) * (s - self.side1) * (s - self.side2) * (s - self.side3))
    
    def getPerimeter(self):
        return self.side1 + self.side2 + self.side3
    
    def toString(self):
        return 'Triangle: Side1 = {}, Side2 = {}, Side3 = {}, Area = {}, Perimeter = {}'.format(self.side1, self.side2, self.side3, self.getArea(), self.getPerimeter())

a = Triangle(3, 4, 5)
print(a.toString())