segments = eval(input())
segments = sorted(segments)
start = 0
end = 0
res = 0
for el in segments:
    if(el[0] > end):
        res += end - start
        start = el[0]
        end = el[1]
    elif(el[1] > end):
        end = el[1]
res += end - start
print(res)

