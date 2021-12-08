class Dots:
    start = 0
    end = 0
    def __init__(self, begin, stop):
        self.start = begin
        self.end = stop
    def __getitem__(self, item):
        if not isinstance(item, slice):
            n = item-1
            return (self.start+(self.end-self.start)/n*i for i in range(0, n+1))
        if item.step is None:
            n = item.stop-1
            i = item.start
            return self.start+(self.end-self.start)/n * i
        n = item.step-1
        i = item.start if item.start else 0
        j = item.stop if item.stop else item.step
        return (self.start+(self.end-self.start)/n*i for i in range(i, j))
    
