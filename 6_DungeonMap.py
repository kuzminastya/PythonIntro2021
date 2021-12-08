i = 0
dungeons = []
paths = {}
entry, out = '', ''
while i < 2:
    s = input().split()
    if len(s) == 1:
        if i == 0:
            entry = s[0]
        if i == 1:
            out = s[0]
        i += 1
    else:
        paths.setdefault(s[0], set()).add(s[1])
        paths.setdefault(s[1], set()).add(s[0])

entryset = set()
entryset.add(entry)
check = set()
check.add(entry)

while out not in entryset:
    entry = check.pop()
    old_len = len(entryset)
    if entry in paths.keys():
        for v in paths[entry]:
            entryset.add(v)
            check.add(v)
            paths[v].remove(entry)
        del paths[entry]
    if old_len == len(entryset) and len(check) == 0:
        break

print('YES') if (out in entryset) else print('NO')
