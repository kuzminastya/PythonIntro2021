def superposition(funmod, funseq):
    res = []
    for fun in funseq:
        def f(x, g=fun):
            return funmod(g(x))
        res.append(f)
    return res
