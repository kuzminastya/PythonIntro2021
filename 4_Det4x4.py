def det2(s1, s2):
    return s1[0]*s2[1] - s1[1]*s2[0]

def det3(s1, s2, s3):
    r1 = (s2[1], s2[2])
    r2 = (s3[1], s3[2])
    res = s1[0] * det2(r1, r2)
    r1 = (s2[0], s2[2])
    r2 = (s3[0], s3[2])
    res -= s1[1] * det2(r1, r2)
    r1 = (s2[0], s2[1])
    r2 = (s3[0], s3[1])
    res += s1[2] * det2(r1, r2)
    return res

a, b, c, d = eval(input())

res = a[0] * det3(b[1:4], c[1:4], d[1:4])

l1 = (b[0], b[2], b[3])
l2 = (c[0], c[2], c[3])
l3 = (d[0], d[2], d[3])
res -= a[1] * det3(l1, l2, l3)

l1 = (b[0], b[1], b[3])
l2 = (c[0], c[1], c[3])
l3 = (d[0], d[1], d[3])
res += a[2] * det3(l1, l2, l3)

res -= a[3] * det3(b[0:3], c[0:3], d[0:3])

print(res)
