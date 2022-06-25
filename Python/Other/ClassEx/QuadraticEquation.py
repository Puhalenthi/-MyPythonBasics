class QuadEq():
    def __init__(self, a = 1, b = 1, c = 1):
        self.a = a
        self.b = b
        self.c = c
    
    def seta(self, a = 1):
        self.a = a
    
    def setb(self, b = 1):
        self.b = b
    
    def setc(self, c = 1):
        self.c = c
    
    def getDiscriminant(self):
        return (self.b ** 2) - (4 * self.a * self.c)
    
    def getRoot1(self):
        return (-self.b + self.getDiscriminant()) / (2 * self.a)
    
    def getRoot2(self):
        return (-self.b - self.getDiscriminant()) / (2 * self.a)


a = QuadEq(1, 2, 3)

print(a.getRoot1(), a.getRoot2())