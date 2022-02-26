import math
class Point():
    def __init__(self, xcoor, ycoor):
        self.xcoor = xcoor
        self.ycoor = ycoor


class LineSegment(Point):
    def __init__(self, PointA, PointB):
        self.PointA = PointA
        self.PointB = PointB
        self.slopevar = (self.PointB.ycoor - self.PointA.ycoor) / (self.PointB.xcoor - self.PointA.xcoor)

    def endPointA(self):
        return (self.PointA.xcoor, self.PointA.ycoor)
    
    def endPointB(self):
        return (self.PointB.xcoor, self.PointB.ycoor)
    
    def length(self):
        return math.sqrt(((self.PointB.xcoor - self.PointA.xcoor) ** 2) + ((self.PointB.ycoor - self.PointB.ycoor) ** 2))
    
    def toString(self):
        return '({}, {}) --- ({}, {})'.format(self.PointA.xcoor, self.PointA.ycoor, self.PointB.xcoor, self.PointB.ycoor)
    
    def isVertical(self):
        return self.PointA.xcoor == self.PointB.xcoor
    
    def isHorizontal(self):
        return self.PointA.ycoor == self.PointB.ycoor
    
    def isParallel(self, otherLine):
        return self.slopevar == otherLine.slopevar

    def isPerpendicular(self, otherLine):
        return self.slopevar == (1 / (otherLine.slopevar)) * -1

    def slope(self):
        return self.slopevar
    
    def shift(self, xInc = 0, yInc = 0):
        self.PointA.xcoor += xInc
        self.PointA.ycoor += yInc
        self.PointB.xcoor += xInc
        self.PointB.ycoor += yInc
    
    def midpoint(self):
        self.midx = (self.PointA.xcoor + self.PointB.xcoor) / 2
        self.midy = (self.PointA.ycoor + self.PointB.ycoor) / 2

        return '({}, {})'.format(self.midx, self.midy)

a = Point(1, 1)
b = Point(4, 5)

c = Point(14, 19)
d = Point(17, 23)

ls1 = LineSegment(a, b)
ls2 = LineSegment(c, d)

#print(ls1.isParallel(ls2))