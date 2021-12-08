k = int(input())
res = k
num = 0
p = 1
mod, div = 0, 0
prev_num = k
while (res*k != k*(10**(p-1)) + res//10):
    mod = prev_num % 10
    div = prev_num // 10
    num = mod*k + div
    res = res + 10**p*(num % 10)
    prev_num = num
    p = p + 1 
print(res)
