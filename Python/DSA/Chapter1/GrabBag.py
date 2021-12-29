import random
class Bag():
    def __init__(self):
        self.bag = []
    
    def add(self, item):
        self.bag.append(item)
        return self.bag
    
    def grabItem(self):
        self.bag.pop(random.randrange(0, len(self.bag)))
        return self.bag


bag1 = Bag()

for i in range(10):
    print(bag1.add(i))

for i in range(10):
    print(bag1.grabItem())