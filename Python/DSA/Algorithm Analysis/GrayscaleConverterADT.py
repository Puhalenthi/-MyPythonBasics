from RGBColorADT import RGBColor
from pprint import pprint
class GrayscaleImage():
    def __init__(self, nrows, ncols):
        self.nrows = nrows
        self.ncols = ncols
        self.image = [[0] * self.ncols] * self.nrows
    
    def width(self):
        return self.ncols
    
    def height(self):
        return self.nrows
    
    def clear(self):
        for i in range(self.nrows):
            for j in range(self.ncols):
                if self.image[i][j] <= 127.5:
                    self.image[i][j] = 0
                else:
                    self.image[i][j] = 255
    
    def getitem(self, row, col):
        return self.image[row][col]
    
    def setitem(self, row, col, value):
        self.image[row][col] = value
        return self.image

    def colorToGrayscale(self, colorImg):
        self.image = [[0] * colorImg.width] * colorImg.height
        for i in range(colorImg.height):
            for j in range(colorImg.width):
                r, g, b = colorImg.image[i][j]
                val = round((0.299 * r) + (0.587 * g) + (0.114 * b))
                self.image[i][j] = val
        
        return self.image

    


img = GrayscaleImage(5, 5)

rgb = RGBColor(4, 4)
rgb.clear((45, 87, 192))
rgb.setitem(1, 3, (1, 3, 5))
rgb.setitem(2, 2, (8, 123, 4))
rgb.setitem(3, 1, (214, 23, 123))
rgb.setitem(1, 2, (97, 236, 0))
pprint(img.colorToGrayscale(rgb))