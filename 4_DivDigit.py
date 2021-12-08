def divdigit(n):
    res = 0
    for ch in str(n):
        if (int(ch) != 0) and (n%(int(ch)) == 0):
            res += 1
    return res
