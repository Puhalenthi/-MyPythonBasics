class Queue():
    def __init__(self):
        self.q = []
        return self.q
    
    def enqueue(self, elem):
        self.q.insert(0, elem)
        return self.q
    
    def dequeue(self):
        self.q.pop(0)
        return self.q
    def length(self):
        return len(self.q)
    
    def isEmpty(self):
        if self.q == []:
            return True
        else:
            return False