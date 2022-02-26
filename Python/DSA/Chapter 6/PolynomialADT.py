class Poly():
    def __init__(self, coef, var, pow):
        self.coef = coef
        self.var = var
        self.pow = pow
    
    def returnterm(self):
        return '{}{}\u00b{}'.format(self.coef, self.var, self.pow)
    
    def add(self, other):
        if self.var == other.var and self.pow == other.pow:
            return '{}{}\u00b{}'.format(self.coef + other.coef, self.var, self.pow)
        else:
            return '{}{}\u00b{} + {}{}\u00b{}'.format(self.coef, self.var, self.pow, other.coef, other.var, other.pow)
    
    def sub(self, other):
        if self.var == other.var and self.pow == other.pow:
            return '{}{}\u00b{}'.format(self.coef - other.coef, self.var, self.pow)
        else:
            return '{}{}\u00b{} - {}{}\u00b{}'.format(self.coef, self.var, self.pow, other.coef, other.var, other.pow)
    
    def mul(self, other):
        if self.var == other.var:
            return '{}{}\u00b{}'.format(self.coef * other.coef, self.var, self.pow + other.pow)
        else:
            return '{}{}\u00b{}{}\u00b{}'.format(self.coef * other.coef, self.var, self.pow, other.var, other.pow)
