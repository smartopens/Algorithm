import sys
sys.setrecursionlimit(10**6)
n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
ans = [[0]*n for _ in range(n)]
vi = [[0]*n for _ in range(n)]
flag = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1
for a in graph:
    for j in range(n):
        if j == n-1:
            print(a[j])
            continue

        print(a[j], end = ' ')