s = input()
pattern = input()
ptrn = pattern.split('@')
res = -1
start = 0
j = 0
while len(ptrn[j]) == 0:
    start += 1
    j += 1
    if(j == len(ptrn)):
        res = 0 if j < len(s) else -1
        j = 0
        start = 0
        break
found = False
for k in range(s.count(ptrn[j])):
    if found:
        break
    idx = s.find(ptrn[j], start)
    res = idx
    for i in range(j+1, len(ptrn)):
        idx += len(ptrn[i-1]) + 1
        if not s[idx:].startswith(ptrn[i]):
            res = -1
            break
    if res > -1:
        found = True
    start = s.find(ptrn[j], start) + len(ptrn[j])
print(res - j if (res-j) > -2 else -1)
