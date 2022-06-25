from math import pi, sqrt


class Circle():
    def __init__(self, x = 0, y = 0, radius = 1):
        self.x = x
        self.y = y
        self.radius = radius
    
    def area(self):
        return (self.radius ** 2) * pi
    
    def perimeter(self):
        return 2 * self.radius * pi
    
    def containspoint(self, px, py):
        self.distance = sqrt(((px - self.x) ** 2) + ((py - self.y) ** 2))
        if self.distance <= self.radius:
            return True
        else:
            return False
    
    def containscircle(self, circ2):
        self.centerdistance = sqrt(((circ2.x - self.x) ** 2) + ((circ2.y - self.y) ** 2))
        if self.centerdistance + circ2.radius <= self.radius:
            return True
        else:
            return False
    
    def overlaps(self, circ2):
        if self.containscircle(circ2):
            return False
        elif self.centerdistnce >= self.radius and self.centerdistace <= self.radius + circ2.radius:
            return True
