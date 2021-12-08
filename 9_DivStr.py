class DivStr(str):
    def __init__(self, s):
        self.s = s
    def __floordiv__(self, n):
        l = len(self.s) // n
        if l > 0:
            return [DivStr(self.s[i:i+l]) for i in range(0,l*n,l)]
        else:
            return [DivStr('') for i in range(n)]
    def __mod__(self, n):
        l = len(self.s) % n
        if l > 0:
            return DivStr(self.s[-(l):])
        else:
            return DivStr('')
    def __getitem__(self, key):
        return DivStr(super().__getitem__(key))
    def __add__(sekf, other):
        return DivStr(super().__add__(other))
    def __mul__(sekf, other):
        return DivStr(super().__mul__(other))
    def __rmul__(sekf, other):
        return DivStr(super().__rmul__(other))
    def capitalize(self):
        return DivStr(super().capitalize())
    def casefold(self):
        return DivStr(super().casefold())
    def center(self, width, fillchar=' '):
        return DivStr(super().center(width, fillchar))
    def expandtabs(self, tabsize=8):
        return DivStr(super().expandtabs(tabsize))
    def format(self, *args, **kwargs):
        return DivStr(super().format(*args, **kwargs))
    def format_map(self, mapping):
        return DivStr(super().format_map(mapping))
    def join(self, iterable):
        return DivStr(super().join(iterable))
    def ljust(self, width, fillchar=' '):
        return DivStr(super().ljust(width, fillchar))
    def lower(self):
        return DivStr(super().lower())
    def lstrip(self, chars=' '):
        return DivStr(super().lstrip(chars))
    def removeprefix(self, prefix):
        return DivStr(super().removeprefix(prefix))
    def removesuffix(self, suffix):
        return DivStr(super().removesuffix(suffix))
    def replace(self, old, new, count=-1):
        return DivStr(super().replace(old, new, count))
    def rjust(self, width, fillchar=' '):
        return DivStr(super().rjust(width, fillchar))
    def rstrip(self, chars=' '):
        return DivStr(super().rstrip(chars))
    def strip(self, chars=' '):
        return DivStr(super().strip(chars))
    def swapcase(self):
        return DivStr(super().swapcase())
    def title(self):
        return DivStr(super().title())
    def translate(self, table):
        return DivStr(super().translate(table))
    def upper(self):
        return DivStr(super().upper())
    def zfill(self, width):
        return DivStr(super().zfill(width))
    
    
    
    
