import random
class Bag():
    def __init__(self):
        self.set = []

    def fill(self, size, From, To):
        for _ in range(size):
            self.add(random.randrange(From, To))
        
        return self.set

    def change(self, index, element):
        self.set[index] = element
        return self.set
    
    def add(self, element):
        self.set.append(element)
        return self.set
    
    def removeByIndex(self, index):
        del self.set[index]
        return self.set

    def removeByElement(self, element):
        counter = 0
        for i in self.set:
            if i == element:
                del self.set[counter]

            counter += 1
        
        return self.set
    
    def count(self):
        uniquelist = []

        for i in self.set:
            if i not in uniquelist:
                uniquelist.append(i)
        
        return len(uniquelist)

a = Bag()

print(a.fill(10, 1, 100))