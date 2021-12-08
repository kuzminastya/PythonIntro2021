from collections import namedtuple

s = input().split()
d = {}
Point = namedtuple('Point', ['x', 'y', 'z'])
res = [0, '', '']
while(len(s) > 1):
    p = Point(float(s[0]), float(s[1]), float(s[2]))
    d[p] = s[3]
    for p1 in d.keys():
        r = (p.x-p1.x)*(p.x-p1.x) + (p.y-p1.y)*(p.y-p1.y) + (p.z-p1.z)*(p.z-p1.z)
        if r > res[0]:
            res[0] = r
            res[1] = d[p]
            res[2] = d[p1]
    s = input().split()

print(*sorted(res[1:]))
