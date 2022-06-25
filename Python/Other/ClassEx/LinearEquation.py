class LinEq():
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
    
    def __solvex(self):
        x = ((self.e * self.d) - (self.b * self.f)) / ((self.a * self.d) - (self.b * self.c))
        return x
    
    def __solvey(self):
        y = ((self.a * self.f) - (self.e * self.c)) / ((self.a * self.d) - (self.b * self.c))
        return y
    
    def getPoint(self):
        return (self.__solvex(), self.__solvey())

p1 = LinEq(9, 4, 3, -5, -6, -21)
print(p1.getPoint())