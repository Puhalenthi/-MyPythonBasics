class Queue():
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element):
        self.queue.insert(0, element)
    
    def dequeue(self):
        del self.queue[-1]
    
    def empty(self):
        if self.queue == []:
            return True
        
        return False
    
    def getSize(self):
        return len(self.queue)
