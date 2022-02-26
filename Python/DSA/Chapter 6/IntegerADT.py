class Integer():
    def __init__(self, val=0):
        self.val = val
    
    def tostring(self):
        self.string = str(self.val)
        return self.string
    
    def compare(self, other):
        if self.val < other.val:
            return '{} is less than {}'.format(self.var, other.val)
        elif self.val > other.val:
            return '{} is greater than {}'.format(self.var, other.val)
        else:
            return '{} is equal than {}'.format(self.var, other.val)
    
    def arithmetic(self, other, sign):
        if sign.count('=') == 0:
            if sign == '+':
                return self.val + other.val
            elif sign == '-':
                return self.val - other.val
            elif sign == '*':
                return self.val * other.val
            elif sign == '//':
                return self.val // other.val
            elif sign == '%':
                return self.val % other.val
            elif sign == '**':
                return self.val ** other.val
            else:
                return 'Please choose another sign'
        else:
            if sign == '+=':
                self.val += other.val
            elif sign == '-=':
                self.val -= other.val
            elif sign == '*=':
                self.val *= other.val
            elif sign == '//=':
                self.val //= other.val
            elif sign == '%=':
                self.val %= other.val
            elif sign == '**=':
                self.val **= other.val
            else:
                return 'Please choose another sign'
            
            return self.val
    
    