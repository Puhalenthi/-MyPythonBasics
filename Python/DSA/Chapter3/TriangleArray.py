import random
class triangle():
    def __init__(self, height, width, length):
        self.height, self.width, self.length = height, width, length
        self.array = [[[0] * self.length] * self.width] * self.height
    
    def fill(self):
        for a in range(self.height):
            for b in range(self.width):
                for c in range(self.length):
                    self.array[a][b][c] = random.randint(0, 100)
    
    def returnarray(self):
        return self.array

a = triangle(3, 3, 3)
a.fill()

print(a.returnarray())