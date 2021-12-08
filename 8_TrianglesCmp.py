from math import sqrt

class Triangle:
    a = 0
    b = 0
    c = 0
    def __init__(self, x, y, z):
        self.a, self.b, self.c = float(x), float(y), float(z)
    def __bool__(self):
        if self.a<=0 or self.b<=0 or self.c<=0:
            return False
        if self.a >= self.b+self.c or self.b >= self.a+self.c or self.c >= self.a+self.b:
            return False
        return True
    def __abs__(self):
        if not self.__bool__():
            return 0
        p = (self.a+self.b+self.c)/2
        return sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
    def __eq__(self, other):
        s = [self.a, self.b, self.c]
        o = [other.a, other.b, other.c]
        for el in s:
            if el in o:
                o.pop(o.index(el))
            else:
                return False
        return True
    def __ne__(self, other):
        return abs(self) != abs(other)
    def __ge__(self, other):
        return abs(self) >= abs(other)
    def __le__(self, other):
        return abs(self) <= abs(other)
    def __gt__(self, other):
        return abs(self) > abs(other)
    def __lt__(self, other):
        return abs(self) < abs(other)
    def __str__(self):
        return f"{self.a}:{self.b}:{self.c}"
