class Vector():
    def __init__(self):
        self.array = []
    
    def length(self):
        self.counter = 0
        for _ in self.array:
            self.counter += 1
        
        return self.counter
    
    def contains(self, item):
        done = False
        for i in self.array:
            if i == item:
                done = True
                break
        return done
    
    def getitem(self, ndx):
        return self.array[ndx]
    
    def setitem(self, ndx, item):
        self.array[ndx] = item
        return self.array
    
    def append(self, item):
        self.array += [item]
    
    def insert(self, ndx, item):
        self.array += [None]
        for i in range(len(self.array)-1, ndx, -1):
            self.array[i + 1] = self.array[i]
        
        self.array[ndx] = item
        return self.array
    
    def remove(self, ndx):
        for i in range(ndx + 1, len(self.array)):
            self.array[i-1] = self.array[i]
        
        return self.array
    
    def indexOf(self, item):
        counter = 0
        for i in self.array:
            if i == self.array:
                break
            counter += 1
        return counter
    
    def extend(self, otherVector):
        self.array += otherVector
        return self.array
    
    def subVector(self, From, To):
        return self.array[From:To + 1]
    
    def __iterator__(self):
        return self.array