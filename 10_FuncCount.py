from functools import wraps

def counter(fun):
    total = 0
    def c():
        nonlocal total
        return total
    @wraps(fun)
    def newfun(*args, **kwargs):
        nonlocal total
        total += 1
        return fun(*args, **kwargs)
    newfun.counter = c
    return newfun
