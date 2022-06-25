import time
class Stopwatch():
    def __init__(self):
        self.start = 0
        self.end = 0
    
    def startclock(self):
        self.start = round(time.time() * 1000)
    
    def endclock(self):
        self.end = round(time.time() * 1000)
    
    def gettime(self):
        return self.end - self.start

a = Stopwatch()

a.startclock()

time.sleep(2)

a.endclock()

print(a.gettime())