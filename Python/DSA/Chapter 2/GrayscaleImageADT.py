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
    


img = GrayscaleImage(5, 5)