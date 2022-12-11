from collections import defaultdict

n, k = map(int, input().split(' '))

worth = [[0]*(k+1) for _ in range (n + 1)]
for i in range(1, n + 1):
    w, v = map(int, input().split(' '))
    for j in range (1, k+1):
        if j < w :
            worth[i][j] = worth[i-1][j]
        else:
            worth[i][j] = max(worth[i-1][j], worth[i-1][j-w] + v)

print(worth[n][k])
