class Timer:
    existingtimers = 0
    def __init__(self, h, m, s):
        Timer.existingtimers += 1
        self.h = h
        self.m = m
        self.s = s
        self.nh =  self.h
        self.nm = self.m
        self.ns = self.s

        self.org()

        self.h = self.nh
        self.m = self.nm
        self.s = self.ns

    def __str__(self):
        return f'{self.h} : {self.m} : {self.s} {Timer.existingtimers}'

    def next_second(self):
        self.nh =  self.h
        self.nm = self.m
        self.ns = self.s

        self.ns += 1

        print(self.org())

    def prev_second(self):
        self.ns -= 1

        if self.ns == -1:
            self.ns = 60
            self.nm -= 1
        if self.nm == -1:
            self.nm = 60
            self.nh -= 1
        if self.nh == -1:
            self.nh = 24
        
        return f'{self.nh} : {self.nm} : {self.ns} {Timer.existingtimers}'

    def org(self):
        if self.ns == 60:
            self.ns = 0
            self.nm += 1
        if self.nm == 60:
            self.nm = 0
            self.nh += 1
        if self.nh == 24:
            self.nh = 0
    
        return f'{self.nh} : {self.nm} : {self.ns} {Timer.existingtimers}'


for _ in range(3):
    timer = Timer(0, 0, 20)
    print(timer)
    timer.next_second()
    print(timer)
    timer.prev_second()