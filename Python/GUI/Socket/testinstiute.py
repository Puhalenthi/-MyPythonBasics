'''class Timer:
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

timer = Timer(0, 0, 20)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
timer = Timer(0, 0, 20)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
timer = Timer(0, 0, 20)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()''''''
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.newquad()

    def newquad(self):
        if self.x < 0:
            if self.y < 0:
                self.quad = 3
            else:
                self.quad = 2
        else:
            if self.y < 0:
                self.quad = 4
            else:
                self.quad = 1

        if self.quad == 1:
            self.strquad = '1st'
        elif self.quad == 2:
            self.strquad = '2nd'
        elif self.quad == 3:
            self.strquad = '3rd'
        else:
            self.strquad = '4th'

    def chgpoint(self, x, y):
        self.x = x
        self.y = y
        self.newquad()

    def __str__(self):
        return f'The Point ({self.x}, {self.y} is a point located in the {self.strquad} quadrant)'
    
    def __add__(self, other):
        return f'The Points ({self.x}, {self.y}) and ({other.x}, {other.y}) has been added to get the resulting Point of ({self.x + other.x}, {self.y + other.y})'
    
    def __sub__(self, other):
        return f'The Points ({self.x}, {self.y}) and ({other.x}, {other.y}) has been subtracted to get the resulting Point of ({self.x - other.x}, {self.y - other.y})'
    
    def __mul__(self, other):
        return f'The Points ({self.x}, {self.y}) and ({other.x}, {other.y}) has been multiplied to get the resulting Point of ({self.x * other.x}, {self.y * other.y})'
    
    def __truediv__(self, other):
        return f'The Points ({self.x}, {self.y}) and ({other.x}, {other.y}) has been divided to get the resulting Point of ({self.x / other.x}, {self.y / other.y})'

a = Point(10, 20)
b = Point(25, 30)

print(a + b)
print(a - b)
print(a * b)
print(a / b)'''

counter = 0

for i in range(1, 1001):
    if i % 4 == 0 and i % 6 == 0 and i % 7 != 0:
        counter += 1
        print(i)

print(counter)