from cmath import pi, tan


class RegPoly():
    def __init__(self, n = 3, s = 1):
        self.n = n
        self.s = s
    
    def area(self):
        self.a = (self.n * (self.s ** 2)) / (4 * (tan(pi / self.n)))
    
    def perim(self):
        self.p = self.n * self.s
    
    def __str__(self):
        return 'A regular polygon with {} sides, each measuring {} units, has an area of {} and a perimeter of {}'.format(self.n, self.s, self.a, self.p)

a = RegPoly(6, 4)
b = RegPoly(10, 4)

a.area()
a.perim()
b.area()
b.perim()

print(a)
print(b)