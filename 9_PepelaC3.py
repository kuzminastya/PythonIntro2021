try:
    s = input().split(' ')
    while len(s[0]) < 2:
        if len(s) < 3 and s[1].isupper():
            s.append('')
        elif len(s) < 3 and s[1].islower():
            s.append(s[1])
            s[1] = ''
        if len(s[1]) > 1:
            locals()[s[0]] = type(s[0], (eval(','.join(s[1]))), {'det': s[2]})
        elif len(s[1]) > 0:
            locals()[s[0]] = type(s[0], (eval(','.join(s[1])),), {'det': s[2]})
        else:
            locals()[s[0]] = type(s[1], (), {'det': s[2]})
        s = input().split(' ')

    locals()['New'] = type('New', (eval(','.join(s[0]))), {'det': s[1]})
    need = s[2]
    for el in need:
        if not any([el in c.det for c in New.mro()[:-1]]):
            print('Incorrect')
            break
    else:
        print('Correct')
except:
    print('Incorrect')
