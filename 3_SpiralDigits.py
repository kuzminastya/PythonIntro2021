m, n = eval(input())
line = [-1 for i in range(m)]
matrix = [line.copy() for i in range(n)]
direction = 'right' 
x, y = 0, 0
for i in range(n*m):
    matrix[x][y] = i%10
    if(direction == 'right'):
        if(y == m-1 or matrix[x][y+1] != -1):
            x += 1
            direction = 'down'
        else:
            y += 1
    elif(direction == 'down'):
        if(x == n-1 or matrix[x+1][y] != -1):
            y += -1
            direction = 'left'
        else:
            x += 1
    elif(direction == 'left'):
        if(y == 0 or matrix[x][y-1] != -1):
            x += -1
            direction = 'up'
        else:
            y += -1
    elif(direction == 'up'):
        if(x == 0 or matrix[x-1][y] != -1):
            y += 1
            direction = 'right'
        else:
            x += -1

for i in range(n):
    print(*matrix[i])
