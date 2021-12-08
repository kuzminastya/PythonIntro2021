class Tester:
    def __init__(self, fun):
        self.f = fun
    def __call__(self, suite, allowed=[]):
        al = 0
        fo = 0
        for el in suite:
            try:
                r = self.f(*el)
            except Exception as e:
                if any(isinstance(e, el) for el in allowed):
                    al += 1
                else:
                    fo += 1
        if al == 0 and fo == 0:
            return 0
        elif fo > 0:
            return 1
        elif al > 0:
            return -1
