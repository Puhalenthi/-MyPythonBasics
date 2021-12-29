class Set:
    def __init__(self):
        self.set = []

    def length(self):
        counter = 0
        for i in self.set:
            counter += 1
        return counter

    def contains(self, element):
        return element in self.set

    def add(self, element):
        if element not in self.set :
            self.set.append(element)

    def remove(self, element):
        if element in self.set:
            self.set.remove(element)

    def __eq__(self, setB):
        if len(self.set) != len(setB) :
            return False
        else :
            return self.isSubsetOf(setB)


    def isSubsetOf(self, setB):
        for element in self :
            if element not in setB :
                return False
        return True

    def union(self, setB):
        newSet = Set()
        newSet.set.extend(self.set)
        for element in setB :
            if element not in self :
                newSet.set.append(element)
        return newSet

    def __iter__( self ):
        return self.set