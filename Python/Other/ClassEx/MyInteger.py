class MyInteger():
    def __init__(self, v):
        self.v = v
    
    def isEven(self):
        return self.v % 2 == 0
    
    def isOdd(self):
        return self.v % 2 != 0
    
    def isPrime(self):
        for i in range(2, self.v - 1):
            if self.v % i == 0:
                return False
        
        return True
    
    def equals(self, c):
        return self.v == c
    
    def setv(self, v):
        self.v = v

a = MyInteger(10)
print(a.isEven())
print(a.isOdd())
print(a.isPrime())
print(a.equals(3))

print()

b = MyInteger(97)
print(b.isEven())
print(b.isOdd())
print(b.isPrime())
print(b.equals(97))