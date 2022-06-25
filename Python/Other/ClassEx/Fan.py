class Fan():
    def __init__(self, speed = 'slow', on = False, radius = 5, color = 'blue'):
        self.speed = speed
        self.on = on
        self.radius = radius
        self.color = color
    
    def changespeed(self, speed):
        self.speed = speed
    
    def changeon(self, on):
        self.on = on
    
    def changeradius(self, radius):
        self.radius = radius
    
    def changecolor(self, color):
        self.color = color
    
    def __str__(self):
        if self.on:
            return 'The fan\'s speed is {}, color is {}, and has a radius of {}'.format(self.speed, self.color, self.radius)
        else:
            return 'The fan\'s color is {}, has a radius of {}, and is turned off'.format(self.color, self.radius)

a = Fan('fast', True, 10, 'yellow')
b = Fan('medium', False)

print(a)
print(b)