from itertools import groupby

def seq(s):
    g = groupby(s)
    n = []
    for el in g:
        n.append(len(list(el[1])))
        n.append(int(el[0]))
    return n

def LookSay():
    n = [1]
    while 1:
        yield from n
        n = seq(n)
