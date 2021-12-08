import sys
import random

N = int(input())
txt = sys.stdin.read().replace("\n    ", " @ ").split()
d = {}
for i in range(len(txt)-2):
    d.setdefault(txt[i], []).append((txt[i+1], txt[i+2]))
first = random.choice(txt)
second, third = random.choice(d[first])
print(first,second,third, end=" ")
for i in range(N-3):
    first = second
    second = third
    third = random.choice([item[1] for item in d[first] if item[0]==second])
    if third == "@":
        print("\n    ", end=" ")
    else:
        print(third, end=" ")
    
