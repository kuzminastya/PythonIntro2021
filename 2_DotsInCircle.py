x, y, r = eval(input())
a, b = eval(input())
res = False
while a != 0 or b != 0:
    if (a-x)**2 + (b-y)**2 > r**2:
        break
    a, b = eval(input())
else:
    res = True
print('YES' if res == True else 'NO')
