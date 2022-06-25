class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.newquad()

    def newquad(self):
        if self.x < 0:
            if self.y < 0:
                self.quad = 3
            else:
                self.quad = 2
        else:
            if self.y < 0:
                self.quad = 4
            else:
                self.quad = 1

        if self.quad == 1:
            self.strquad = '1st'
        elif self.quad == 2:
            self.strquad = '2nd'
        elif self.quad == 3:
            self.strquad = '3rd'
        else:
            self.strquad = '4th'

    def chgpoint(self, x, y):
        self.x = x
        self.y = y
        self.newquad()

    def __str__(self):
        return f'The Point ({self.x}, {self.y} is a point located in the {self.strquad} quadrant)'
    
    def __add__(self, other):
        return f'The Points ({self.x}, {self.y}) and ({other.x}, {other.y}) has been added to get the resulting Point of ({self.x + other.x}, {self.y + other.y})'
    
    def __sub__(self, other):
        return f'The Points ({self.x}, {self.y}) and ({other.x}, {other.y}) has been subtracted to get the resulting Point of ({self.x - other.x}, {self.y - other.y})'
    
    def __mul__(self, other):
        return f'The Points ({self.x}, {self.y}) and ({other.x}, {other.y}) has been multiplied to get the resulting Point of ({self.x * other.x}, {self.y * other.y})'
    
    def __truediv__(self, other):
        return f'The Points ({self.x}, {self.y}) and ({other.x}, {other.y}) has been divided to get the resulting Point of ({self.x / other.x}, {self.y / other.y})'

a = Point(10, 20)
b = Point(25, 30)

print(a + b)
print(a - b)
print(a * b)
print(a / b)