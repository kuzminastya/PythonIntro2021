from fractions import Fraction
from itertools import repeat

class Sausage:
    def __init__(self, nmeat='pork!', nv=1):
        self.v = Fraction(nv) if Fraction(nv) > 0 else Fraction(0)
        self.meat = nmeat
    def __mul__(self, other):
        return Sausage(self.meat, self.v * other)        
    def __rmul__(self, other):
        return Sausage(self.meat, self.v * other) 
    def __truediv__(self, other):
        return Sausage(self.meat, self.v / other) 
    def __add__(self, other):
        return Sausage(self.meat, self.v + other.v)
    def __sub__(self, other):
        return Sausage(self.meat, self.v - other.v)
    def __abs__(self):
        return self.v   
    def __bool__(self):
        return self.v != 0
    def __str__(self):
        n = (self.v).__trunc__()
        ost = int(((self.v) - n)*12)
        s1 = ('/' + '-'*12 + '\\') * n
        s = ('|' + (self.meat*12)[0:12] + '|') * n
        s2 = ('\\' + '-'*12 + '/') * n
        sost1 = '/' + '-'*ost + '|' if (not n or ost) else ''
        sost = '|' + (self.meat*ost)[0:ost] + '|' if (not n or ost)  else ''
        sost2 = '\\' + '-'*ost + '|' if (not n or ost) else ''
        return s1+sost1+'\n'+(s+sost+'\n')*3+s2+sost2
