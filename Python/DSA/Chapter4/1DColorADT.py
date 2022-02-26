from pprint import pprint
class OneDimensionArray():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.prod = self.height * self.width
        self.red = [0] * (self.prod)
        self.green = [0] * (self.prod)
        self.blue = [0] * (self.prod)
    
    def Red(self):
        return self.red
    
    def Green(self):
        return self.green

    def Blue(self):
        return self.blue
    
    def Width(self):
        return self.width
    
    def Height(self):
        return self.height
    
    def clear(self, color):
        r, g, b = color
        for i in range(self.prod):
            self.red[i] = r
            self.green[i] = g
            self.blue[i] = b
        
        return self.red, self.green, self.blue
    
    def getitem(self, row, col):
        elem = (row * self.width) + col
        return (self.red[elem], self.green[elem], self.blue[elem])
    
    def setitem(self, row, col, color):
        r, g, b = color
        elem = (row * self.width) + col
        self.red[elem], self.green[elem], self.blue[elem] = r, g, b
        return self.red, self.green, self.blue


a = OneDimensionArray(5, 7)
print(a.Red())
print(a.Green())
print(a.Blue())
print(a.Width())
print(a.Height())
pprint(a.clear((65, 98, 123)))
print(a.getitem(4, 3))
pprint(a.setitem(3, 1, (34, 255, 0)))
print(a.getitem(3, 1))