class Set:
    def __init__(self): # Initializes the instance and creates a list with the methods and functionality of a set
        self.set = []

    def length(self): # Returns the length of the set
        counter = 0
        for i in self.set:
            counter += 1
        return counter

    def contains(self, element): # Checks if a given element is in the set
        return element in self.set

    def add(self, element): # Adds an element to the set
        if element not in self.set :
            self.set.append(element)

    def remove(self, element): # Removes an element fromt the set
        if element in self.set:
            self.set.remove(element)

    def isSubsetOf(self, setB): # Checks if the current list is a subset of another list
        for element in self :
            if element not in setB :
                return False
        return True

    def union(self, setB): # Returns a list with the elements that are common from both sets
        newSet = Set()
        newSet.set.extend(self.set)
        for element in setB :
            if element in self :
                newSet.set.append(element)
        return newSet

    def sorting(self): # Sorts the set using the Bubble Sort Algorithm
        self.preset = []
        while True:
            for i in range(len(self.set)):
                if i == len(self.set) - 1:
                    continue
                if self.set[i] > self.set[i+1]:
                    self.set[i], self.set[i+1] = self.set[i+1], self.set[i]
            
            if self.preset == self.set:
                break
            self.preset = self.set.copy()
    
        return self.set

    def __eq__(self, setB): # Checks if two sets are equal
        if len(self.set) != len(setB) :
            return False
        else :
            return self.isSubsetOf(setB)