from itertools import compress

def joinseq(*seq):
    seq = [iter(s) for s in seq]
    tmp = [next(it) for it in seq]
    t = list(compress(tmp, [el != -1 for el in tmp]))
    while len(t):
        m = min(t)
        yield m
        idx = tmp.index(m)
        tmp[idx] = next(seq[idx], -1)
        t = list(compress(tmp, [el != -1 for el in tmp]))
