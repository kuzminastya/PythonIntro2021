class Lock:
    
    def locked(cls):
        cls.semaphors = {}
        cls._lock = None
        
        @property
        def x(self):
            if self._lock not in self.semaphors:
                return None
            elif self.semaphors[self._lock] == None or self.semaphors[self._lock] == self.hash:
                self.semaphors[self._lock] = self.hash
                return self._lock
            else:
                return None
        
        @x.setter
        def x(self, name):
            self._lock = name
            self.hash = hash(self)
            if self.hash in self.semaphors.values():
                key = list(self.semaphors.keys())[list(self.semaphors.values()).index(self.hash)]
                self.semaphors[key] = None
            if name not in self.semaphors:
                self.semaphors[name] = None
            
                
        @x.deleter
        def x(self):
            if self._lock in self.semaphors and self.semaphors[self._lock] == self.hash:
                self.semaphors[self._lock] = None

        def newdel(self):
            if self._lock in self.semaphors and self.semaphors[self._lock] == self.hash:
                self.semaphors[self._lock] = None
            if '__del__' in dir(super(type(self), self)):
                super().__del__(self)
        cls.__del__ = newdel
        cls.lock = x
        return cls
