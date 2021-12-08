n, m = eval(input())
w = len(str(n))*2 + len(str(n*n)) + 8
count = m // w
while m - (count*w + count - 2) < 0:
    count -= 1
for i in range(m):
    print('=', end='')
print()
col = count
line = n
rows = round(n/count + 0.499)
prob_mn = len(str(n))
prob_pr = len(str(n*n))
first, second = 1, 1
for i in range(rows):
    for j in range(n):
        for k in range(count):
            if(first > n):
                for l in range(w):
                    print(' ', end='')
            else:
                if first%count == 1 or first == count == 1:
                    print(f'{first:>{prob_mn}} * {second:<{prob_mn}} = {first*second:<{prob_pr}} ', end='')
                else:
                    print(f'| {first:>{prob_mn}} * {second:<{prob_mn}} = {first*second:<{prob_pr}} ', end='')
            first += 1
        first -= count
        second += 1
        print()
    second -= n
    first += count
    for i in range(m):
        print('=', end='')
    print()
