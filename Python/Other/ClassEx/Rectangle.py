class Rec():
    def __init__(self, width = 1, height = 1):
        self.width = width
        self.height = height
    
    def getarea(self):
        return self.width * self.height
    
    def getperim(self):
        return 2 * (self.width + self.height)

a = Rec(4, 40)
b = Rec(3.5, 35.9)

print(a.getarea(), a.getperim())
print(b.getarea(), b.getperim())