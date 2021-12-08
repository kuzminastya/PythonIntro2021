from random import randint
from itertools import cycle, starmap

def randomes(seq):
    s = []
    for el in seq:
        e = list(el)
        s.append(e)
        yield randint(e[0], e[1])
    while 1:
        yield from starmap(randint, cycle(s))
