a = int(input())
b = a
res = False
length = 0
while b//10 != 0:
    length += 1
    b //= 10
while a//10 != 0:
    if(a//(10**length) != a%10):
        break
    a -= a//(10**length) * 10**length
    length -= 2
    a //= 10
else:
    res = True
print('YES' if res == True else 'NO')
