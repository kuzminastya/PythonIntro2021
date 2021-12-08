import math
n = int(input())
res = True
i = 2
while i < n:
    if math.log(n, i) - int(math.log(n, i)) == 0.0:
        break
    i += 1
else:
    res = False
print('YES' if res == True else 'NO')
