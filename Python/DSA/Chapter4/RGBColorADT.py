from pprint import pprint
class RGBColor():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.image = [[(0, 0, 0)] * self.width] * self.height
    
    def widthfunc(self):
        return self.width
    
    def heightfunc(self):
        return self.height
    
    def clear(self, color):
        for i in range(self.height):
            for j in range(self.width):
                self.image[i][j] = color
        
        return self.image
    
    def getitem(self, row, col):
        return self.image[row][col]
    
    def setitem(self, row, col, color):
        self.image[row][col] = color
        return self.image

if __name__ == '__main__':
    a = RGBColor(4, 6)

    print(a.widthfunc())
    print('+-----+')
    print(a.heightfunc())
    print('+-----+')
    pprint(a.clear((231, 134, 12)))
    print('+-----+')
    print(a.getitem(1, 3))
    print('+-----+')
    pprint(a.setitem(3, 4, (1, 3, 5)))
    print('+-----+')
    print(a.getitem(3, 4))
    print('+-----+')