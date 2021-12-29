class Fraction():
    def __init__(self, num, den):
        self.num = num
        self.den = den
    
    def toString(self):
        return '{}/{}'.format(self.num, self.den)
    
    def toDec(self):
        return self.num/self.den
    
    def reciprocal(self):
        return '{}/{}'.format(self.den, self.num)
    
    def isTerminatingDecimal(self):
        self.newden = self.den
        while True:
            if self.newden % 2 == 0:
                self.newden /= 2
            elif self.newden % 5 == 5:
                self.newden /= 5
            elif self.newden == 1:
                answer = True
                break
            else:
                answer = False
                break
        return answer

a = Fraction(10, 3)

print(a.toString())
print(a.toDec())
print(a.reciprocal())
print(a.isTerminatingDecimal())