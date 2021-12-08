from math import sqrt

seq = set(eval(input()))
m = max(seq)
squares = set()
for i in range(1, int(sqrt(m))+1):
    for j in range(i, int(sqrt(m-i*i))+1):
        for k in range(j, int(sqrt(m-i*i-j*j))+1):
            squares.add(i*i+j*j+k*k)
res = seq & squares
print(len(res))
