def sizer(cls):
    cls.size = None
    
    @property
    def x(self):
        tmp = 0
        if '__len__' in dir(self):
            tmp = cls.__len__(self)
        elif '__abs__' in dir(self):
            tmp = cls.__abs__(self)
        return tmp
        
    cls.size = x
    
    return cls
