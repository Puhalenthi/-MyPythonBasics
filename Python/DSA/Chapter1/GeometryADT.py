import math
from LineSegmentADT import LineSegment

class Polygon():
    def __init__(self, *points):
        self.points = points
    
    def anglesum(self):
        return 180 * (len(self.pointspoints) - 2)
    
    def perim(self):
        total = 0
        for i in range(len(self.points)):
            if i == len(self.points)-1:
                total += math.sqrt(((self.points[0][0] - self.points[i][0]) ** 2) + ((self.points[0][1] - self.points[i][1]) ** 2))
            else:
                total += math.sqrt(((self.points[i+1][0] - self.points[i][0]) ** 2) + ((self.points[i+1][1] - self.points[i][1]) ** 2))
        
        return total
        
a = Polygon((0, 0), (4, 0), (4, 3))

print(a.perim())