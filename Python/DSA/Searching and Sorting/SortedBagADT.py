import random
class Bag():
    def __init__(self): # Initalizes the instance and creates a list
        self.bag = []
    
    def add(self, item): # Adds an item to the bag
        self.bag.append(item)
        return self.bag
    
    def grabItem(self): # Removes a random item fromt he bag
        self.bag.pop(random.randrange(0, len(self.bag)))
        return self.bag
    
    def sorting(self): # Sort the bag from the numeric least to greatest value using the Bubble Sort algorithm
        self.prebag = []
        while True:
            for i in range(len(self.bag)):
                if i == len(self.bag) - 1:
                    continue
                if self.bag[i] > self.bag[i+1]:
                    self.bag[i], self.bag[i+1] = self.bag[i+1], self.bag[i]
            
            if self.prebag == self.bag:
                break
            self.prebag = self.bag.copy()
    
        return self.bag

a = Bag()
a.add(2)
a.add(4)
a.add(1)
a.add(434)
a.add(31)
a.add(0)
a.add(-3)
a.add(7)
print(a.sorting())