import random

class Bag:
    def __init__(self):
        self.bag = []
    
    def add(self, x):
        self.bag.append(x)
        return self.bag
    
    def grabItem(self):
        self.bag.pop(random.randrange(0, len(self.bag)))
        return self.bag
    
    def numOf(self, item):
        self.counter = 0
        for i in self.bag:
            if i == item:
                self.counter += 1
        
        return 'The element, {}, is in the bag {} times'.format(item, self.counter)

bag1 = Bag()

for _ in range(50):
    print(bag1.add(random.randrange(0, 10)))

for num in range(10):
    print(bag1.numOf(num))

for _ in range(50):
    print(bag1.grabItem())