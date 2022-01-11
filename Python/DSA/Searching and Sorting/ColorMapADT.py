class ColorMap():
    def __init__(self, size): # Initializes the instance and creates a list with a fixed size
        self.size = size
        self.colors = [[] for _ in range(self.size)]
    
    def length(self): # Returns the amount of colors and spaces of memory left on the ColorMap
        counter = 0
        for i in self.colors:
            if i != []:
                counter += 1
        
        return 'There are {} colors in the ColorMap and {} spaces of memory left'.format(counter, self.size - counter)
    
    def contains(self, checkcolor): # Checks if the given color is in the ColorMap
        if checkcolor in self.colors:
            return True
        else:
            return False

    def add(self, addcolor): # Adds a color to the ColorMap
        if self.contains(addcolor) == True:
            return 'Item already exists'
        
        for i in range(self.size):
            if self.colors[i] == []:
                self.colors[i] = addcolor
                break
        
        return self.colors
    
    def remove(self, removecolor): # Removes a color from the ColorMap
        if self.contains(removecolor) == False:
            return 'Item does not exist'
        
        self.colors[self.map(removecolor)] = []
        
        return self.colors
    
    def changecolor(self, prechangecolor, newchangecolor): # Changes a color from the Color
        if self.contains(prechangecolor) == False:
            return 'Item does not exist'
        
        self.colors[self.map(prechangecolor)] = newchangecolor

        return self.colors
    
    def map(self, findcolor): # Returns the index of a color from the ColorMap
        return self.colors.index(findcolor)
    
    def __iter__(self): # Returns an iterator for the colors
        return self.colors

a = ColorMap(10)
print(a.length())
print(a.add([4, 7, 1]))
print(a.add([67, 8, 1]))
print(a.add([4, 4, 4]))
print(a.add([7, 32, 1]))
print(a.add([234, 8, 1]))
print(a.add([234, 4, 30]))
print(a.length())
print(a.remove([4, 4, 4]))
print(a.remove([4, 7, 1]))
print(a.changecolor([234, 8, 1], [99, 100, 101]))
print(a.map([67, 8, 1]))
print(a.length())