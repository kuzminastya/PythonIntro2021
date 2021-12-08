from itertools import chain, islice

def chainslice(begin, end, *seq):
    return islice(chain.from_iterable(list(seq)), begin, end)
