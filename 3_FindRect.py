s1 = list(input())
field = []
prev_str = []
res = 0
s = list(input())
while s != s1:
    field.append(s)
    hashes = [i for i in range(len(s)) if s[i]=='#']
    for h_idx in hashes:
        if(not prev_str or not(h_idx in prev_str)):
            if h_idx > 0 and h_idx < len(s)-1:
                if not(h_idx-1 in hashes):
                    res += 1
    prev_str = hashes
    s = list(input())

print(res)
