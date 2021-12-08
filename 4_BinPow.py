def BinPow(a, n, f):
    if (n == 1):
        return a
    if (n % 2 == 1):
        return f(BinPow (a, n-1, f), a)
    else:
        b = BinPow (a, n/2, f)
        return f(b, b)
