def squares(w, h, *seq):
    out = [['.' for i in range(w)] for j in range(h)]
    for el in seq:
        x, y, s, c = el
        for i in range(y, y+s):
            for j in range(x, x+s):
                out[i][j] = c

    for j in range(h):
        for i in range(w):
            print(out[j][i], end = '')
        print()
