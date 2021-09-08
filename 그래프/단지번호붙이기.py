import sys

sys.setrecursionlimit(100000)

n = int(input())

visited = [[False] * n for _ in range(n)]
arr = []
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(x, y):
    global cnt
    visited[x][y] = True
    cnt += 1

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny]:

            if not (visited[nx][ny]):
                visited[nx][ny] = True
                dfs(nx, ny)


for _ in range(n):
    arr.append(list(map(int, input().strip())))

result = []
gr_num = 0

for i in range(n):
    for j in range(n):
        cnt = 0
        if not (visited[i][j]) and arr[i][j]:
            dfs(i, j)
            gr_num += 1

            if cnt:
                result.append(cnt)
result.sort()
print(gr_num)
for i in result:
    print(i)
