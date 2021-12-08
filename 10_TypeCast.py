from functools import wraps

def cast(totype):
    def dcr(fun):
        @wraps(fun)
        def wrapper(*args, **kwargs):
            return totype(fun(*args, **kwargs))
        return wrapper
    return dcr
